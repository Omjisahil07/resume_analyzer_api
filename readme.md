# Resume Analyzer API

A Django-based API that provides functionalities for resume analysis. This API can be used for analyzing resumes, extracting information, and performing other tasks related to resume processing.

## Requirements

- Python 3.x
- Django 3.x or higher
- Django REST framework (if needed for API views)
- Other dependencies (listed below)

## Installation Steps

### 1. Clone the Repository

Clone the repository to your local machine or server:

```bash
git clone <repository_url>
cd <project_directory>
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment to keep your project dependencies isolated:

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, you can manually install Django and other dependencies:

```bash
pip install django
# Any other dependencies like django-rest-framework can be added similarly:
# pip install djangorestframework
```

### 4. Set Up the Database

Run the following commands to set up your database:

```bash
# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### 5. Run the Development Server

Run the server on port 8080:

```bash
python manage.py runserver 8080
```

Your server should now be running at `http://127.0.0.1:8080/`.

### 6. Create Superuser (Optional)

If you want to access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your superuser credentials.

### 7. Access the API

Now, you can access the API at the following URL:

- `http://127.0.0.1:8080/api/your-endpoint/`

Where `/your-endpoint/` should be replaced with the appropriate endpoint from your `urls.py`.

---

## Folder Structure

```bash
resume_analyzer_api/
├── analyzer/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── resume_analyzer_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── manage.py
├── requirements.txt
└── README.md
```

### Key Files:

- **`manage.py`**: Command-line utility to interact with the Django project.
- **`analyzer/models.py`**: Contains the models for the app (if needed).
- **`analyzer/views.py`**: Contains the API views (where the main logic for resume analysis can be added).
- **`analyzer/urls.py`**: Contains URL routing for the API endpoints.
- **`resume_analyzer_api/settings.py`**: Main settings file for the project.
- **`resume_analyzer_api/urls.py`**: The root URL configuration for the project.

---

## Common Issues

### 1. Server not starting on port 8080

Make sure no other application is already using port 8080. If it is, either stop that application or run the server on another port:

```bash
python manage.py runserver 8000
```

### 2. Missing Migration Errors

If you encounter migration-related errors, try running the following commands:

```bash
# To reset migrations
python manage.py migrate --fake <app_name> zero
python manage.py makemigrations
python manage.py migrate
```

### 3. CORS Issues (For API Requests)

If you plan to make requests to the API from another domain, make sure to install and configure `django-cors-headers`:

```bash
pip install django-cors-headers
```

Then, add `'corsheaders.middleware.CorsMiddleware'` to the `MIDDLEWARE` list in your `settings.py` file:

```python
MIDDLEWARE = [
    # Other middleware...
    'corsheaders.middleware.CorsMiddleware',
]
```

---

## Future Improvements

- Implementing resume parsing functionality using NLP models.
- Adding user authentication (JWT, OAuth).
- Integrating file upload functionality for resume files (PDF, DOCX).
- Unit tests for better test coverage.

---

https://github.com/Omjisahil07/resume_analyzer_api