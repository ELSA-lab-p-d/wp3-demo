# Federated Logistic Regression (ELSA WP3 Task 3.3)

This repository contains a federated logistic regression implementation built on the vantage6 framework, together with a Jupyter Notebook that demonstrates how early-warning (vroegsignalering) analyses can be performed across multiple data environments without sharing or centralising raw individual-level data.

The notebook illustrates how statistical models can be estimated jointly using distributed data from different parties, while preserving data separation and governance constraints.

The current version works entirely with synthetic data and is intended for experimentation, validation of the federated workflow, and demonstration of analytical feasibility.

---

## Requirements

To run the code in this repository you need:

- Python 3.9 or higher
- vantage6 (client and algorithm tools)
- Jupyter Notebook

All required Python packages are listed in `requirements.txt`.

---

## Installation

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .LR
source .LR/bin/activate
