from fastapi import FastAPI

# Create FastAPI app instance
app = FastAPI()

# Home Route
@app.get("/")
def home():
    return {"Message": "Hello World"}