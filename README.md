## Demo
https://www.loom.com/share/96253fbeaa2a4ef3a278f95990fe1b36?sid=e7676e0f-b35a-477e-b498-c680f0b7a59a 


'''
## Structure
Login/
├── manage.py            # Main entry point for the application
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (e.g., secret keys)
├── .gitignore           # Files and directories ignored by Git
├── src/                 # Core application code
│   ├── __init__.py      # App initialization
│   ├── accounts/        # User account-related functionality
│   │   ├── __init__.py
│   │   ├── models.py    # Account database models
│   │   ├── views.py     # Account views (routes and logic)
│   │   ├── forms.py     # Forms for user login and registration
│   ├── core/            # Core app logic
│   │   ├── __init__.py
│   │   ├── views.py     # Main app views (e.g., homepage)
│   ├── todo/            # To-do list module
│   │   ├── __init__.py
│   │   ├── models.py    # To-do list database models
│   │   ├── views.py     # To-do list views (routes and logic)
│   │   ├── forms.py     # Forms for adding/editing tasks
│   ├── templates/       # HTML templates for the app
│   │   ├── base.html    # Base layout for all pages
│   │   ├── errors/      # Error pages
│   │   │   ├── 401.html
│   │   │   ├── 404.html
│   │   │   ├── 500.html
│   │   ├── accounts/    # Account-related pages
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   ├── core/        # Core pages
│   │   │   ├── home.html
│   │   ├── todo/        # To-do list pages
│   │       ├── list.html
│   │       ├── add_list.html
│   │       ├── view_list.html
│   │       ├── add_item.html
│   │       ├── edit_item.html
│   ├── static/          # Static files (CSS, JS, images)
│       ├── css/
│           ├── styles.css
├── migrations/          # Database migrations (e.g., Alembic)
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   ├── versions/
│       ├── <migration_files>.py
├── tests/               # Unit tests for the app
│   ├── __init__.py
│   ├── base_test.py
│   ├── test_forms.py
│   ├── test_models.py
│   ├── test_routes.py
├── venv/                # Virtual environment for dependencies
    ├── bin/
    ├── lib/
    ├── include/
'''



## Built with
- Python
- Flask
- SQLite
- Javascript


<!-- INSTALLATION -->

## Installation

1. Clone the repo
   ```sh
   git clone
   ```
2. Create a virtual environment (Conda, Pipenv, etc.). Optional but recommended.
   ```sh
   pip create -n venv python
   pip activate venv
   ```   


#### Installation

1. Install the requirements
   ```sh
   pip install -r requirements.txt
   ```
2. Open 'src' folder
   ```sh
   cd src
   ```
3. Run the app
   ```sh
   python manage.py run
   ```
4. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) to view it in the browser. 

<br><br>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

