"""
Run this once to create the local SQLite database tables and seed an admin user.
Usage: python seed_db.py
"""
from FlaskWebProject import app, db
from FlaskWebProject.models import User, Post

with app.app_context():
    db.create_all()
    print("✅ Tables created.")

    # Create admin user if not exists
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin')
        admin.set_password('pass')
        db.session.add(admin)
        db.session.commit()
        print("✅ Admin user created. Login: admin / pass")
    else:
        print("ℹ️  Admin user already exists.")

    print("✅ Database ready!")
