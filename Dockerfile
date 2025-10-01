# 공식 Ubuntu 20.04 이미지를 베이스로 사용합니다.
FROM ubuntu:20.04

# 설치 중 발생하는 상호작용 프롬프트를 방지하기 위한 환경 변수 설정
ENV DEBIAN_FRONTEND=noninteractive

# 패키지 리스트를 업데이트하고 필요한 시스템 및 파이썬 패키지들을 한 번에 설치합니다.
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    python3 \
    python3-pip \
    python3-numpy \
    python3-scipy \
    python3-tk \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# pip를 최신 버전으로 업그레이드합니다.
RUN python3 -m pip install --upgrade pip

# 필요한 파이썬 패키지들을 pip로 설치합니다.
RUN pip install matplotlib line_profiler snakeviz memory_profiler Pillow

# 작업 디렉토리 설정
WORKDIR /app

# 소스 코드 복사
COPY . .

# 컨테이너 실행 시 기본 명령어
CMD ["python3", "/app/W4.py"]
