from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "Welcome to FastAPI!"

@app.get("/data")
def data():
    return {
        "data": {
            "name": "Bhavik Jikadara",
            "Age": 24,
            "Gender": "Male"
        }
    }
