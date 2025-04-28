.venv\Scripts\activate
pip install -r requirements.txt
uvicorn api.main:app --reload
