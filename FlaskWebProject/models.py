from datetime import datetime
from FlaskWebProject import app, db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from werkzeug.utils import secure_filename
from flask import flash
from azure.storage.blob import BlobServiceClient
import string, random, os

blob_container = app.config['BLOB_CONTAINER']
blob_account   = app.config['BLOB_ACCOUNT']
blob_key       = app.config['BLOB_STORAGE_KEY']

if blob_account and blob_key:
    blob_service = BlobServiceClient(
        account_url=f"https://{blob_account}.blob.core.windows.net",
        credential=blob_key
    )
else:
    blob_service = None

def id_generator(size=32, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id            = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

class Post(db.Model):
    __tablename__ = 'posts'
    id         = db.Column(db.Integer, primary_key=True)
    title      = db.Column(db.String(150))
    author     = db.Column(db.String(75))
    body       = db.Column(db.String(800))
    image_path = db.Column(db.String(100))
    timestamp  = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id    = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

    def save_changes(self, form, file, userId, new=False):
        self.title   = form.title.data
        self.author  = form.author.data
        self.body    = form.body.data
        self.user_id = userId

        if file and file.filename:
            filename      = secure_filename(file.filename)
            fileextension = filename.rsplit('.', 1)[1]
            random_filename = id_generator() + '.' + fileextension
            try:
                if blob_service:
                    # Delete old blob if exists
                    if self.image_path:
                        try:
                            blob_service.get_blob_client(
                                container=blob_container,
                                blob=self.image_path
                            ).delete_blob()
                        except Exception:
                            pass
                    # Upload new blob
                    blob_client = blob_service.get_blob_client(
                        container=blob_container,
                        blob=random_filename
                    )
                    blob_client.upload_blob(file, overwrite=True)
                    self.image_path = random_filename
            except Exception as e:
                flash(str(e))

        if new:
            db.session.add(self)
        db.session.commit()
