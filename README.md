📝 FastAPI Notes App

Simple CRUD Notes Application built with:

FastAPI

MongoDB

Jinja2

python-dotenv
dotenv

🚀 Setup Guide (Windows)
1️⃣ Clone Repository
git clone https://github.com/your-username/notes_app.git
cd notes_app
2️⃣ Create Virtual Environment
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
Create .env File
Inside project root create a file named:
.env
MONGO_URL=mongodb://localhost:27017/
DB_NAME=notes_db
uvicorn main:app --reload

