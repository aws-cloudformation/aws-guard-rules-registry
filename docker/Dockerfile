
FROM rust:alpine

RUN apk add --no-cache cargo tree
RUN cargo install cfn-guard
ENV PATH "/root/.cargo/bin:${PATH}"

COPY ./output/ /
