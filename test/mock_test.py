from vantage6.algorithm.tools.mock_client import MockAlgorithmClient
from pathlib import Path
import os
import sys

###############################################################
# Generate dataset
###############################################################

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_person(number_of_records:int):
    subtractionDays = np.random.randint(1,365)
    startDate = (datetime.today() - timedelta(days=subtractionDays)).date()
    addition_days_since_start = np.random.randint(0,subtractionDays, size=number_of_records)
    
    dates = []
    for x in addition_days_since_start:
        myDate = (startDate + timedelta(days=x.item()))
        dates.append(myDate)
    
    debtAmount = np.random.randint(100,5000,size=(number_of_records))
    
    person_frame = pd.DataFrame(list(zip(dates, debtAmount)), columns = ["debt_date", "amount"])
    return person_frame.sort_values(by="debt_date")

result_set = generate_person(np.random.randint(1,10))
result_set["person_id"] = 0
for i in range(100):
    new_set = generate_person(np.random.randint(1,10))
    new_set['person_id'] = i+1
    result_set = pd.concat([result_set, new_set], ignore_index=True)

result_set.to_csv("data.csv", index=False)

###############################################################

# get path of current directory
current_path = Path(os.getcwd())#.parent
parent_path = current_path.parent
current_path = os.path.abspath(current_path)

# add folder to library path
sys.path.append(os.path.join(str(parent_path), "researcher", "algorithms", "count"))

## Mock client
client = MockAlgorithmClient(
    datasets=[
        # Data for first organization
        [{
            "database": os.path.join(current_path,  "data.csv"),
            "db_type": "csv",
            "input_data": {}
        }]
    ],
    # package name where main method is present
    module="count_citizens"
)

# list mock organizations
organizations = client.organization.list()
org_ids = [organization["id"] for organization in organizations]

# 1. Wat is de incidentie van apendicities (D88=D88) en cholelithiasis (D98 / D98*)?
#   - incidentie:=episodes nieuw gestart in 2022
central_task = client.task.create(
    input_ = {
        "method":"count_citizens",
        "master": True
        },
    organizations=[org_ids[0]],
)
results = client.wait_for_results(central_task.get("id"))

print(results)