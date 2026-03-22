# Recycling Waste System

A Django web application for users to submit waste or recycling items with images, descriptions, and locations. Includes user authentication and an admin dashboard.

## Features

- User registration and login
- Submit waste/recycle items with description, location, image upload, and type selection
- Admin dashboard to view all submitted items
- Bootstrap-styled interface

## Setup

1. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

2. Run migrations:

   ```
   python manage.py migrate
   ```

3. Create superuser:

   ```
   python manage.py createsuperuser
   ```

4. Run the server:
   ```
   python manage.py runserver
   ```

Access the app at http://127.0.0.1:8000

Admin at http://127.0.0.1:8000/admin

## Requirements

- Python 3.8+
- Django 4.2+
- Pillow
