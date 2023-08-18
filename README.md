# ELSA Lab WP3a demo

In this demo, we provide an overview of using Privacy-enhancing technologies (PET) to analyze current and future data sharing solutions to address poverty and debt.

Specifically, this demo provides an infrastructure and example for analysis where the researcher is unable to access the data however is able to request to execute an analysis and receive the analysis results.

License: see [LICENSE](./LICENSE)

## Prerequisites

The following prerequisites are needed to execute this code:

- Docker Engine (Linux), Docker for Windows or Docker for macOS installed and operational
- Python version 3.7 or higher (including pip)
- 

## How to interpret this repository?

This repository contains an example how PET can be used, specifically using the [Vantage6](https://vantage6.ai) infrastructure. This repository contains code to setup one central server, one node, and one algorithm for testing purposes.

### Infrastructure
The folder [infrastructure](./infrastructure) contains information to setup the infrastructure. More information about the infrastructure can be found in this folder.
The scripts [setup.sh](./setup.sh) and [shutdown.sh](shutdown.sh) can be used to setup and shutdown the infrastructure.

### Analysis

A sample analysis is available in the [researcher](researcher/) folder. This contains an algorithm to count the number of citizens over multiple sources. The code for this federated analysis is available in [researcher/algorithms/count](researcher/algorithms/count) and the execution code is available in [researcher/execution/count.ipynb](researcher/execution/count.ipynb).

Please mind this is a fictive example and is intended to show how the infrastructure works.