from fastapi import FastAPI #FastAPI is a class 
from routers import metrics
from routers import aws
app = FastAPI(
    title="DevOps Utilities API",
    description="A collection of utilities for DevOps tasks, including file management and system monitoring.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

"""
API always returns a response in JSON format. The response is a dictionary with a single key "message" and 
the value "Hello, World!".
"""


@app.get("/") #@ is a decorator that tells FastAPI that this function should be called when a GET request is made to the /hello endpoint.
def hello():
    return {"message" : "Hello, World!"}


app.include_router(metrics.router)
app.include_router(aws.router, prefix="/aws") 
#we use prefix to group all AWS related endpoints under the /aws path, so the buckets endpoint will be accessible at /aws/buckets.