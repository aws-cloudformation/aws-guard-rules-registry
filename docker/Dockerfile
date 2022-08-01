
FROM ubuntu:22.10
RUN apt-get update && \
  apt-get install -y \
  curl && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*
RUN curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/aws-cloudformation/cloudformation-guard/main/install-guard.sh | sh
ENV PATH "${PATH}:~/.guard/bin"

COPY ./output/ /
