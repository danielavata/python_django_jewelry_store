jewelry_store Project

Short-description:

Jewelry store where you can pick or demand a product/accessory (watches, smartwatches, jewelries for women, men and children)! We will contact YOU!

How to interact with it:

Prerequisites:

Make sure you have the following installed on your machine:

•	Python (3.12 recommended)

•	Pip (Python package installer) (24.0 recommended): py -m pip install --upgrade pip

•	Virtualenv (optional but recommended for isolating dependencies)


1. Navigate to the project directory:

cd your-repo

2. Create a virtual environment (optional but recommended):

python -m venv venv

3. Activate the virtual environment:

.\venv\Scripts\activate #Windows
source venv/bin/activate #macOS/Linux

4. Install project dependencies:

pip install -r requirements.txt

5. Create project folder:

django-admin startproject "your-project-name"

6. Create application:

python manage.py startapp "your-application-name"

7. Apply migrations:

python manage.py makemigrations
python manage.py migrate

8. Create a superuser (for Django Admin):

python manage.py createsuperuser

9. Run the development server:

python manage.py runserver

Replace placeholders like "your-project-name", "your-username", "your-repo", "your-application-name", etc., with your actual project information.
Access the application at: http://127.0.0.1:8000/
