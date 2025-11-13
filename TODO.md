# TODO: Integrate Django Backend for LMS Project

## Step 1: Install Django
- [x] Check if Django is installed using `pip list`.
- [x] Django 5.2.7 is installed.

## Step 2: Create Django Project
- [x] Create a new directory 'lms_django' in the current working directory.
- [x] Run `python -m django startproject lms .` to create the project in the root directory.

## Step 3: Configure Django Settings
- [x] Edit lms/settings.py: Set up database (use SQLite), add static files and templates directories pointing to existing HTML/CSS/JS.
- [x] Add 'accounts' to INSTALLED_APPS, and create accounts app for LMS functionality.

## Step 4: Create Django Models
- [x] Create a new app, 'accounts' using `python manage.py startapp accounts`.
- [x] Define User model in accounts/models.py based on PHP logic (email, password, userType, subject).

## Step 5: Create Views for Serving HTML and Handling Login
- [x] In accounts/views.py, create views to render existing HTML files (e.g., login.html, admin_home.html).
- [x] Implement login view to handle POST, authenticate user, and redirect based on userType.

## Step 6: Configure URLs
- [x] Edit lms/urls.py and accounts/urls.py to map URLs to views.
- [x] Update any form actions in HTML files to point to Django URLs (minimal changes to HTML).

## Step 7: Migrate Database and Create Superuser
- [x] Run `python manage.py makemigrations` and `python manage.py migrate`.
- [x] Create a superuser if needed for admin.

## Step 8: Test the Application
- [x] Run `python manage.py runserver` and test login and page serving.
- [x] Ensure redirects work as before (e.g., admin to admin_home.html).
- [x] Verified login authentication with redirects for admin, trainer, and trainee user types.
- [x] Tested serving of multiple HTML pages (e.g., admin_home.html, student_home.html, trainer dashboards).
- [x] Confirmed static files (CSS, JS) are loading correctly on pages.
- [x] Tested edge cases like invalid login credentials.

## Step 9: Final Adjustments
- [x] Move or copy HTML files to templates directory if rendering as templates.
- [x] Ensure static files (CSS, JS) are served correctly.
- [x] Copied all CSS and JS files to static directory for proper serving.
- [x] Updated all HTML files to use {% static %} template tags for CSS and JS links.
