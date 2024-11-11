# AI server

AI 서빙을 위한 레포지토리입니다.
- python==3.11.10

## 환경설정
```
# 가상환경 생성
conda create -n bio-ai python=3.11.10

# 가상환경 활성화
conda activate bio-ai

# 패키지 설치
pip install -r requirements.txt

# 서버 실행 (root 디렉토리에서)
uvicorn src.main:app --reload
```

## local swagger 접속
- uvicorn 실행 후 접속 가능합니다.
- http://localhost:8000/docs
