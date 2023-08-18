# Demo infrastructure

The infrastructure contains two components:

1. A central message broker (server)
2. A node which containing a dataset

## Central message broker

The configuration for the central message broker is available in [server](server). Specifically, it contains a configuration file for the server ([server/wp3server.yaml](server/wp3server.yaml)) and a file to load organisations, users and collaborations for demo purposes ([server/entities.yaml](server/entities.yaml)). In a production scenario, this entities.yaml would not exist, and no hard-coded passwords/tokens will be used.

More information about the server configuration can be found here: [https://docs.vantage6.ai/en/main/server/configure.html](https://docs.vantage6.ai/en/main/server/configure.html)

## Node containing a dataset

The node configuration is available in the [inforing](inforing) folder. This folder contains a configuration (template) file for the node ([inforing/template.yaml](inforing/template.yaml)) and a python script which generates a fictive data example ([inforing/prepare.py](inforing/prepare.py)).

More information about the node configuration can be found here: [https://docs.vantage6.ai/en/main/node/configure.html](https://docs.vantage6.ai/en/main/node/configure.html)