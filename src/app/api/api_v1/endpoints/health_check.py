from fastapi import APIRouter


router = APIRouter()


@router.get("/{check}")
def health_check(check: str):
    return {"message": f"Check OK. Get {check} param"}
