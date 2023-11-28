import pandas as pd
import time
from vantage6.tools.util import info
import json

def count_citizens(client, data):
    info('Collecting participating organizations')

    organizations = client.get_organizations_in_my_collaboration()
    ids = [organization.get("id") for organization in organizations]

    info('Requesting partial computation')
    task = client.create_new_task(
        input_={
            'method': 'count_citizens'
        },
        organization_ids=ids
    )

    info("Waiting for results")
    task_id = task.get("id")
    task = client.get_task(task_id)
    while not task.get("complete"):
        task = client.get_task(task_id)
        info("Waiting for results")
        time.sleep(1)

    # Once we now the partials are complete, we can collect them.
    info("Obtaining results")
    results = client.get_results(task_id=task.get("id"))

    count = 0
    for result in results:
        count += result['citizen_count']
    
    return {"total_citizen_count": count}

def RPC_count_citizens(data):
    info("In the requested method")
    info(f"the dataset contains {len(data.index)} rows")
    info(f"count: {data['person_id'].nunique()}")
    result_dict = get_template_json()
    result_dict["results"] = {
        "citizen_count": data['person_id'].nunique()
    }
    return json.dumps(result_dict, indent=2)

def get_template_json():
    {
        "dashboard":
            [
            {
                "type": "bar",
                "title": "Acquisitions by year (bar)",
                "data": {
                "x": [2010, 2011, 2012, 2013, 2014, 2015, 2016],
                "datasets": [
                    {
                    "label": "Dataset 1",
                    "y": [10, 20, 15, 25, 22, 30, 28]
                    },
                    {
                    "label": "Dataset 2",
                    "y": [3, 14, 32, 21, 6, 7, 11]
                    }
                ]
                }
            },
            {
                "type": "line",
                "title": "Acquisitions by year (line)",
                "data": {
                "x": [2010, 2011, 2012, 2013, 2014, 2015, 2016],
                "datasets": [
                    {
                    "label": "Dataset 1",
                    "y": [10, 20, 15, 25, 22, 30, 28]
                    },
                    {
                    "label": "Dataset 2",
                    "y": [3, 14, 32, 21, 6, 7, 11]
                    }
                ]
                }
            },
            {
                "type": "bubble",
                "title": "Acquisitions by year (bubble)",
                "data": {
                "x": [2010, 2011, 2012, 2013, 2014, 2015, 2016],
                "datasets": [
                    {
                    "label": "Dataset 1",
                    "y": [10, 20, 15, 25, 22, 30, 28],
                    "r": [20, 5, 40, 6, 1, 16, 11]
                    },
                    {
                    "label": "Dataset 2",
                    "y": [10, 7, 34, 19, 2, 6, 25],
                    "r": [10, 5, 2, 6, 15, 27, 30]
                    }
                ]
                }
            },
            {
                "type": "radar",
                "title": "Acquisitions by year (radar)",
                "data": {
                "x": [2010, 2011, 2012, 2013, 2014, 2015, 2016],
                "datasets": [
                    {
                    "label": "Dataset 1",
                    "y": [10, 20, 15, 25, 22, 30, 28]
                    },
                    {
                    "label": "Dataset 2",
                    "y": [3, 14, 32, 21, 6, 7, 11]
                    }
                ]
                }
            },
            {
                "type": "pie",
                "title": "Acquisitions by year (pie)",
                "data": {
                "x": [2010, 2011, 2012, 2013, 2014, 2015, 2016],
                "y": [10, 20, 15, 25, 22, 30, 28]
                }
            },
            {
                "type": "doughnut",
                "title": "Acquisitions by year (doughnut)",
                "data": {
                "x": [2010, 2011, 2012, 2013, 2014, 2015, 2016],
                "y": [10, 20, 15, 25, 22, 30, 28]
                }
            },
            {
                "type": "polarArea",
                "title": "Acquisitions by year (polarArea)",
                "data": {
                "x": [2010, 2011, 2012, 2013, 2014, 2015, 2016],
                "y": [10, 20, 15, 25, 22, 30, 28]
                }
            }
        ]
    }