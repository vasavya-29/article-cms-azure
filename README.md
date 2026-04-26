# Article CMS on Azure

A Content Management System (CMS) for articles built with Python and Flask, fully deployed on Microsoft Azure.

## Overview

This application allows users to log in, view published articles, and publish new articles. Each article consists of a title, author, and body of text stored in **Azure SQL Database**, along with an optional image stored in **Azure Blob Storage**. Authentication supports both standard username/password login and **Sign in with Microsoft** via OAuth2 (Microsoft Entra ID).

## Architecture

- **Web App:** Python 3.10 with Flask framework
- **Database:** Azure SQL Database (users and posts tables)
- **Image Storage:** Azure Blob Storage container
- **Authentication:** Flask-Login + Microsoft Entra ID (OAuth2 / MSAL)
- **Hosting:** Azure App Service (Python 3.10, Free F1 tier)
- **Region:** Central India

## Features

- User login with username and password
- Sign in with Microsoft (OAuth2)
- Create, view, and edit articles
- Image upload to Azure Blob Storage
- Security logging for successful and unsuccessful login attempts

## Deployment

Deployed on Azure App Service. All sensitive credentials are stored as environment variables in the App Service configuration — not hardcoded in the source code.

## Login Credentials

- **Username:** `admin`
- **Password:** `pass`

## Project Requirements Completed

1. Resource Group created in Azure (`cms`)
2. Azure SQL Database created with `users` and `posts` tables, populated via SQL scripts
3. Azure Blob Storage container created for image storage
4. Sign In With Microsoft button implemented using the `msal` library and Microsoft Entra ID
5. Deployment analysis completed in `WRITEUP.md` — chose App Service over VM
6. Logging added for successful and unsuccessful login attempts
7. Article created on live Azure URL with required fields
8. Screenshots captured for all rubric requirements

## Project Structure

```
├── application.py          # App entry point
├── config.py               # Configuration (reads from environment variables)
├── WRITEUP.md              # VM vs App Service analysis
├── requirements.txt        # Python dependencies
├── sql_scripts/
│   ├── users-table-init.sql
│   └── posts-table-init.sql
└── FlaskWebProject/
    ├── __init__.py         # App factory, logging setup
    ├── views.py            # Routes, auth, logging
    ├── models.py           # SQLAlchemy models, Blob Storage
    ├── forms.py            # Flask-WTF forms
    ├── static/             # CSS, JS, images
    └── templates/          # HTML templates
```

## Local Development

```bash
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python application.py
```

App runs at `https://localhost:5555`
