from fastapi import APIRouter , HTTPException
from services.aws_service import get_buckets

router = APIRouter()

@router.get("/s3", status_code=200)
def get_buckets_endpoint():
    try:
        buckets_info = get_buckets()
        return buckets_info
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error: Unable to retrieve bucket information")

