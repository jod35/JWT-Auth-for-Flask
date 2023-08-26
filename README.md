# JWT Authentication for Flask
This is source code for a video I made when demonstrating how to implement JWT Authentication for Flask REST APIs. This videos series walks through the following.
- Project SetUp
- Database Management with Flask-SQLAlchemy
- User Account Creation
- JWT Authentication with Flask-JWT-Extended


# How to run the project
1. Clone the repository
```bash
git clone https://github.com/jod35/JWT-Auth-for-Flask.git && cd JWT-Auth-for-Flask.git/
```

2. Install requirements
```bash
pip install requirements.txt
```

3. Create a `.env` file and set environment variables
```
FLASK_SECRET_KEY=<your-secret-key>
FLASK_DEBUG=<your-debug-boolean-value>
FLASK_SQLALCHEMY_DATABASE_URI=<your-sqlalchemy-db-uri>
FLASK_SQLALCHEMY_ECHO=<your-sqlalchemy-echo-value>
```

4. Create a `FLASK_APP` environment variable. 
```bash
export FLASK_APP=src/
```

5. Create the database by running 
```bash
python3 create_db.py
```