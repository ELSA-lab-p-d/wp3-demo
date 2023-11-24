# python vantage6 algorithm base image
FROM harbor2.vantage6.ai/infrastructure/algorithm-base:3.7.3

# this should reflect the python package name
ARG PKG_NAME="count_citizens"

# install federated algorithm
COPY . /count_citizens
RUN pip install /count_citizens

ENV PKG_NAME=${PKG_NAME}

# Tell docker to execute `docker_wrapper()` when the image is run.
CMD python -c "from vantage6.tools.docker_wrapper import docker_wrapper; docker_wrapper('${PKG_NAME}')"