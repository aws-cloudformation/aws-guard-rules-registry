
FROM ubuntu:22.10
RUN apt-get update && \
  apt-get install -y \
  curl && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*
RUN curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/aws-cloudformation/cloudformation-guard/main/install-guard.sh | sh
# /opt/guard/bin/cfn-guard is a softlink, so we deference it. We don't need other files that way (so no -r)
RUN mkdir -p "/opt/bin" && cp --dereference "/root/.guard/bin/cfn-guard" "/opt/bin/"
ENV PATH "${PATH}:/opt/bin"

COPY ./output/ /
