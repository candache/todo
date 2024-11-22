## Demo
https://www.loom.com/share/96253fbeaa2a4ef3a278f95990fe1b36?sid=e7676e0f-b35a-477e-b498-c680f0b7a59a 


## Structure 
Login/
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── accounts/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── forms.py
│   └── core/
│       ├── __init__.py
│       ├── views.py
│   └── todo/
│       ├── __init__.py
│       ├── models.py
│       ├── views.py
│       ├── forms.py
│   ├── templates/
│       ├── base.html
│       ├── errors/
│           ├── 401.html
│           ├── 404.html
│           ├── 500.html
│       ├── accounts/
│           ├── login.html
│           ├── register.html
│       ├── core/
│           ├── home.html
│       ├── todo/
│           ├── list.html
│           ├── add_list.html
│           ├── view_list.html
│           ├── add_item.html
│           ├── edit_item.html
│   ├── static/
│       ├── css/
│           ├── styles.css
├── migrations/
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   ├── versions/
│       ├── <migration_files>.py
├── tests/
│   ├── __init__.py
│   ├── base_test.py
│   ├── test_forms.py
│   ├── test_models.py
│   ├── test_routes.py
├── venv/
│   ├── bin/
│   ├── lib/
│   ├── include/
│   ├── ...



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

