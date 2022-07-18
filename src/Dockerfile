FROM ubuntu:focal
SHELL ["/bin/bash", "-c"]

RUN DEBIAN_FRONTEND="noninteractive" \
    apt-get update && \
    apt-get install -y python3 python3-distutils curl libgl1 && \
    rm -rf /var/lib/apt/lists/*
RUN python3 <(curl https://bootstrap.pypa.io/get-pip.py)
RUN python3 -m pip install parrot-olympe

COPY ./olympe-scripts/gimbal.py .
ENTRYPOINT [ "python3", "gimbal.py" ]