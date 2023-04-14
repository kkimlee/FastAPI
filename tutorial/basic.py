# Step 1 : import FastAPI
from fastapi import FastAPI 

# Step 2 : create a FastAPI "instance"
app = FastAPI()  

# Step 3 : create a path operation
# Step 4 : define the path operation function
'''
path : "/"
operation : get
function : below the "decoration(@app.get("/"))" 
'''
@app.get("/")
async def root():
    return {"message" : "Hello World"}