# TaskCRUD
Flask based CRUD application for tasks

<!-- Creating Virtual Env -->
python -m virtualenv nameofenv
<!-- Example -->
<!-- python -m virtualenv flaskcrudenv -->

<!-- Enable ENV -->
<!-- In Powershell -->
.\env\Scripts\activate.ps1
<!-- In Command Prompt -->
env\Scripts\activate.bat


<!-- Deactivate ENV -->
deactivate

<!-- RUN APP -->
python .\app.py

<!-- Set up database in terminal -->
<!-- Make sure env is acivated -->
python create_db.py

pip3 install gunicorn
pip3 freeze > requirements.txt