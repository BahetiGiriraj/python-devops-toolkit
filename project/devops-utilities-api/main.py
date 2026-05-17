from app.api import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.api:app",  # The location of the FastAPI application 
        host="127.0.0.1", # local host only for you to access the API on your machine
        # host= "0.0.0.0 ", # allows access to the API from any machine on the network
        port=8000, # The port on which the API will be accessible
        reload=True,
    )