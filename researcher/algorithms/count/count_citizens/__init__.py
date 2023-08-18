import pandas as pd
import time
from vantage6.tools.util import info

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
    return {"citizen_count": data['person_id'].nunique()}