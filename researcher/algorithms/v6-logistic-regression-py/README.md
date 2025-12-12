# Vantage6 Federated Logistic Regression for Early-Warning Analysis

This repository contains a federated logistic regression algorithm designed for the [vantage6](https://vantage6.ai/) privacy-preserving federated learning infrastructure. The algorithm enables multi-party analysis of early-warning debt signal data without centralizing or sharing raw individual-level records.

## Project Overview

This project demonstrates how statistical analyses for early-warning research can be performed across multiple data environments (e.g., BKR and XXLLNC) using federated learning. The algorithm supports:

- **Federated logistic regression**: Training logistic regression models across distributed datasets
- **Privacy preservation**: No raw data exchange between organizations
- **Multi-level analysis**: Both dossier-level and contact-attempt-level analyses
- **Policy evaluation**: Understanding factors that influence contact outcomes in debt signal follow-up processes

### Use Cases

The algorithm is designed to analyze:
1. **Contact establishment (dossier level)**: Whether contact is established at least once for a case
2. **Contact attempt success (contact level)**: Whether individual outreach actions are successful

## Jupyter Notebook Analysis

### Location

The main analysis is contained in the Jupyter notebook:
```
📁 3.3.ipynb
```

### Notebook Contents

The notebook (`3.3.ipynb`) contains:
- **Introduction**: Overview of federated logistic regression for early-warning analysis
- **Experiment 1**: Dossier-level analysis of contact establishment (`is_contact_gelegd` outcome)
- **Experiment 2**: Contact-level analysis of successful contact attempts (`is_succesvol` outcome)
- **Results**: Model coefficients, odds ratios, and validation metrics

Each experiment demonstrates federated execution across multiple data nodes using vantage6.

## Running the Analysis Locally

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository** (if not already done):
   ```bash
   cd /Users/alirezaghavamipour/LR/v6-logistic-regression-py
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install the package and dependencies**:
   ```bash
   pip install -e .
   ```

   This installs the required packages:
   - `vantage6-client` (version 3.7.3)
   - `pandas` (version 1.3.5)
   - `scipy` (version 1.7.3)
   - `scikit-learn` (version 1.0.2)
   - Additional dependencies as specified in `requirements.txt`

4. **Launch Jupyter Notebook**:
   ```bash
   pip install jupyter  # if not already installed
   jupyter notebook 3.3.ipynb
   ```

   This will open the notebook in your default web browser.

5. **Execute the notebook**:
   - Run cells sequentially from top to bottom
   - The notebook uses mock data located in `v6_logistic_regression_py/local/`
   - Both experiments can be executed independently

### Testing with Mock Data

To test the algorithm without Jupyter, you can run the example script:

```bash
python v6_logistic_regression_py/example.py
```

This script:
- Uses mock data from `v6_logistic_regression_py/local/`
- Simulates a federated learning environment with two organizations
- Trains a logistic regression model on distributed data
- Outputs model coefficients and validation metrics

## Input Data Format

The algorithm expects each data node to hold CSV data with the following structure:

### For Dossier-Level Analysis:
- **Predictors**: Demographics (age categories), debt indicators, signal source, number of contact attempts
- **Outcome**: `is_contact_gelegd` (binary: 0 or 1)

### For Contact-Level Analysis:
- **Predictors**: Same as dossier level, plus contact-specific features (contact type, attempt order)
- **Outcome**: `is_succesvol` (binary: 0 or 1)

All categorical variables are one-hot encoded.

## Using the Algorithm in Production

Below is an example of how to run the algorithm in a vantage6 production environment:

```python
import time
from vantage6.client import Client

# Initialize the client
client = Client('http://127.0.0.1', 5000, '/api')
client.authenticate('username', 'password')
client.setup_encryption(None)

# Define algorithm input
input_ = {
    'method': 'master',
    'master': True,
    'kwargs': {
        'org_ids': [2, 3],          # Organizations to run algorithm
        'predictors': [             # Columns to use as predictors
            'leeftijd_26_45',
            'leeftijd_46_65',
            'leeftijd_66_plus',
            'meetbureau_OVERIG',
            'schuld_high',
            'n_pogingen'
        ],
        'outcome': 'is_contact_gelegd',  # Outcome column
        'classes': [0, 1],               # Classes to predict
        'max_iter': 100,                 # Maximum iterations
        'delta': 0.0001,                 # Convergence threshold
    }
}

# Send the task to the central server
task = client.task.create(
    collaboration=1,
    organizations=[2, 3],
    name='v6-logistic-regression-py',
    image='ghcr.io/maastrichtu-cds/v6-logistic-regression-py:latest',
    description='run federated logistic regression',
    input=input_,
    data_format='json'
)

# Retrieve the results
task_info = client.task.get(task['id'], include_results=True)
while not task_info.get('complete'):
    task_info = client.task.get(task['id'], include_results=True)
    time.sleep(1)
result_info = client.result.list(task=task_info['id'])
results = result_info['data'][0]['result']
```

## Repository Structure

```
├── 3.3.ipynb                          # Main analysis notebook
├── Dockerfile                         # Container configuration
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── setup.py                          # Package installation script
├── v6_logistic_regression_py/        # Main package directory
│   ├── __init__.py
│   ├── example.py                    # Local testing script
│   ├── helper.py                     # Helper functions
│   └── local/                        # Mock data for testing
│       ├── data1_contacts.csv
│       ├── data1_dossiers.csv
│       ├── data2_contacts.csv
│       └── data2_dossiers.csv
└── synthetic_output_v1_1/            # Synthetic data outputs
```

## Development Notes

- Developed and tested with Python 3.7
- Uses vantage6 client version 3.7.3
- Implements federated logistic regression using iterative parameter updates
- Supports convergence control via `max_iter` and `delta` parameters

## License

See `LICENSE` file for details.
