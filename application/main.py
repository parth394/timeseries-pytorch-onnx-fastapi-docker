## Libraries
import uvicorn
from fastapi import FastAPI

## Custom Code
from api import api

# Include the router from the main API
app = FastAPI()
app.include_router(api)

if __name__=="__main__":
    uvicorn.run(app, log_level="info")