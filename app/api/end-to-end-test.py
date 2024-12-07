from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class InputProteinName(BaseModel):
    protein_name: str


@router.post("/input-protein-name")
async def input_protein_name(input_protein_name: InputProteinName):
    """
    protein 이름을 받으면 mongodb vector search. -> 약물 구조 생성
    생성된 약물 정보와 protein 정보를 예측 모델에 전달

    결과 반환
    """
    return {"message": "Hello, World!"}
