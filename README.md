# Culinary Recipes - Restaurant Menu Management System

Welcome to the Culinary Recipes project! This is a web-based system for managing culinary recipes, built with a Python web framework. This guide provides all the necessary steps to set up the project locally for development.

This project is built using the following core technologies and libraries:

* **Backend:** Python, Django
* **Database:** PostgreSQL
* **Caching:** Redis
* **Web Server:** Gunicorn, Nginx
* **Deployment:** Docker, AWS
* **Cloud Services:** Cloudinary (for media uploads), Brevo/Anymail (for email sending)
* **Other Libraries:** `django-embed-video`, `requests`, `psycopg2-binary`

---

## Prerequisites

Before you begin, ensure you have the following software installed on your system:

* **Python 3.11:** The specific Python version required for this project.
* **Docker:** Used to run the PostgreSQL and Redis databases in isolated containers.
* **Git:** To clone the project repository.

---

### 1. Clone the Repository

Clone the project from GitHub using the following command:

    git clone https://github.com/Andon-ov/Culinary-Recipes.git

Navigate to the Project Directory
Change your current directory to the main project folder:

    cd Culinary-Recipes/Culinary-Recipes/

### 2. Environment Setup

Create a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies. This isolates the project's packages from your system-wide Python installation.

    python3.11 -m venv venv

Activate the Virtual Environment
Activate the newly created virtual environment based on your operating system:

On Linux/Mac:

    source venv/bin/activate

On Windows:

    venv\Scripts\activate

Install Dependencies
Install all required packages listed in requirements.txt:

    pip install -r requirements.txt
    pip install --upgrade pip

Create Environment Variables
This project uses a .env file to handle environment-specific configurations. Create a file named .env in the root of your project and add the following variables:

### .env file

### Django Secret Key and Debug Settings

    SECRET_KEY='your-django-secret-key'
    DEBUG=True
    ALLOWED_HOSTS='localhost 127.0.0.1'

### Database Configuration (PostgreSQL)

    DB_ENGINE='django.db.backends.postgresql'
    DB_NAME='recipes_db'
    DB_USER='postgres'
    DB_PASSWORD='1123QwER'
    DB_HOST='localhost'
    DB_PORT=5432

### Cloudinary (for image uploads)

    CLOUDINARY_CLOUD_NAME='your_cloudinary_cloud_name'
    CLOUDINARY_API_KEY='your_cloudinary_api_key'
    CLOUDINARY_API_SECRET='your_cloudinary_api_secret'

### Anymail (for email sending via Sendinblue/Brevo)

    API_KEY='your_brevo_api_key'

Note: You can obtain your API keys by creating free accounts on Cloudinary and Brevo (formerly Sendinblue).

### 3. Database Setup (using Docker)

The project uses a PostgreSQL database and a Redis cache. The easiest way to run both services is by using Docker, which provides a clean and isolated environment.

Launch the Database Containers
Run the following commands to start both the PostgreSQL database and Redis cache.

PostgreSQL Container
This command will:

docker run: Create and run a new container.

-p 5432:5432: Map the container's internal port 5432 to your host machine's port 5432.

-e ...: Set environment variables for the database credentials.

-d: Run the container in detached mode (in the background).

--name postgres: Give the container a friendly name for easier management.

-v my-postgres-data:/var/lib/postgresql/data: Create a persistent volume to store your database data.

    docker run -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=1123QwER -e POSTGRES_DB=recipes_db -d -v my-postgres-data:/var/lib/postgresql/data --name postgres postgres:latest

Redis Container
This command will start a Redis container for caching, also running in detached mode:

     docker run -d --name my-redis-cache -p 6379:6379 redis:latest

### Apply Database Migrations

With both database services running, apply the migrations to create the necessary tables for the project:

     python manage.py migrate

### Create a Superuser

Create an administrative user to access the Django admin panel:

     python manage.py createsuperuser

Follow the prompts to set up your username, email, and password.

### 4. Running the Project

Start the Development Server
Finally, start the Django development server to view the project in your browser:

    python manage.py runserver

You can now access the application at http://127.0.0.1:8000/.

### Add the database to your IDE project with the following credentials:

- Username: postgres
- Password: 1123QwER
- Database: recipes_db

### 5. Cleaning Up

When you're finished with the project, you can stop and remove the Docker containers to free up system resources.

### Stop and remove the PostgreSQL container

    docker stop postgres
    docker rm postgres

### Stop and remove the Redis container

    docker stop my-redis-cache
    docker rm my-redis-cache

Warning: To free up storage space, you can also remove the persistent data volumes. This will permanently delete all your database data.

### Delete the PostgreSQL data volume

    docker volume rm my-postgres-data

This guide should help you set up and run the project smoothly. If you have any questions or need further assistance, feel free to reach out. 🚀
