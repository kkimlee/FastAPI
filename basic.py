# Step 1 : import FastAPI
from fastapi import FastAPI 

# Step 2 : create a FastAPI "instance"
app = FastAPI()  

# Step 3 : create a path operation
@app.get("/")
async def root():
    return {"message" : "Hello World"}