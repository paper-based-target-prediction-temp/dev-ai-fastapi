from fastapi import APIRouter

router = APIRouter()


@router.post("/test")
async def get_greetings(input: str):
    """
    router 테스트용 텍스트 입력 api
    """
    return {"님이 넣은 텍스트 ->": input}
