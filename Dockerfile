FROM debian:latest
WORKDIR /home/code

RUN apt-get update && \
    apt-get install -y \
        git \
        python3 \
        python3-venv \
        python3-pip \
        unixodbc && \
    rm -rf /var/lib/apt/lists/*

ENV VIRTUAL_ENV=/home/env
RUN python3 -m venv ${VIRTUAL_ENV}
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY src ./src
COPY data ./data
COPY requirements.txt ./
RUN pip install -r requirements.txt
EXPOSE 8080
