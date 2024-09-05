ARG ALPINE_VERSION=3.20
FROM alpine:${ALPINE_VERSION}
ARG ASDF_VERSION=0.14.1
ARG TERRAFORM_VERSION
ARG TERRAGRUNT_VERSION
ARG USER='cicd-user'

RUN apk update && apk add --no-cache bash curl git

ENV ASDF_HOME=/opt/asdf
ENV ASDF_DATA_DIR=${ASDF_HOME}/data
ENV PATH=${PATH}:${ASDF_HOME}/bin:${ASDF_HOME}/data/shims
RUN git clone https://github.com/asdf-vm/asdf.git ${ASDF_HOME} --branch v${ASDF_VERSION}

RUN    asdf plugin-add terraform                        \
    && asdf plugin-add terragrunt                       \
    && asdf install    terraform  ${TERRAFORM_VERSION}  \
    && asdf install    terragrunt ${TERRAGRUNT_VERSION}

RUN adduser --system --shell /bin/bash --home /app ${USER}

USER ${USER}
WORKDIR /app
RUN    asdf global terraform  ${TERRAFORM_VERSION} \
    && asdf global terragrunt ${TERRAGRUNT_VERSION}
