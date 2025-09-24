# 공식 Ubuntu 20.04 이미지를 베이스로 사용합니다.
FROM ubuntu:20.04

# 설치 중 발생하는 상호작용 프롬프트를 방지하기 위한 환경 변수 설정
ENV DEBIAN_FRONTEND=noninteractive

# 패키지 리스트를 업데이트하고 필요한 패키지들을 설치합니다.
# - python3: 파이썬 인터프리터
# - python3-pip: 파이썬 패키지 설치 도구
# - python3-scipy: 과학 계산용 SciPy 라이브러리
# - python3-numpy: 수치 연산용 NumPy 라이브러리
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-scipy \
    python3-numpy \
    && rm -rf /var/lib/apt/lists/*

# 여기에 line_profiler와 snakeviz를 추가합니다.
RUN pip3 install line_profiler snakeviz matplotlib
