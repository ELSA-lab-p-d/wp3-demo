import pandas as pd
import numpy as np
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
    max_signals = { }
    month_sum_signals = { }
    for result in results:
        count += result['citizen_count']
        
        signal_count =  result["signals_per_citizen"]["signal_count"]
        signal_sum =  result["signals_per_citizen"]["signal_sum"]
        for i in range(0,len(signal_count)):
            i_str = str(signal_count[i])
            
            if i_str in max_signals:
                max_signals[i_str] = max_signals[i_str] + signal_sum[i]
            else:
                max_signals[i_str] = signal_sum[i]
        
        month_id = result["signals_per_month"]["month"]
        month_sum = result["signals_per_month"]["sum"]
        for i in range(0,len(month_id)):
            i_str = month_id[i]
            if i_str not in month_sum_signals:
                month_sum_signals[i_str] = 0
            print(f"sum for month {i_str} with value {month_sum[i]} | {month_sum_signals[i_str]}")
            month_sum_signals[i_str] = month_sum_signals[i_str] + int(month_sum[i])

    result_dict = {
        "dashboard":
            [
            {
                "type": "bar",
                "title": "Signals per Month",
                "data": {
                "x": list(month_sum_signals.keys()),
                "datasets": [
                    {
                    "label": "Dataset 1",
                    "y": list(month_sum_signals.values())
                    }
                ]
                }
            },
            {
                "type": "pie",
                "title": "Signals per citizen / household",
                "data": {
                "x": list(map(int, list(max_signals.keys()))),
                "y": list(max_signals.values())
                }
            }
        ]
    }

    result_dict["results"] = {
        "total_citizen_count": count,
        "signals_per_month": result["signals_per_month"],
        "signals_per_citizen": result["signals_per_citizen"]
        }
    
    return json.dumps(result_dict, indent=2)

def RPC_count_citizens(data):
    info("In the requested method")
    info(f"the dataset contains {len(data.index)} rows")
    info(f"count: {data['person_id'].nunique()}")
    counts = np.unique(data.groupby("person_id").size(), return_counts=True)
    data["debt_date"] = pd.to_datetime(data["debt_date"])
    data["debt_date_string"] = data["debt_date"].dt.strftime("%Y-%m")
    signals_month = data.groupby("debt_date_string").size()
    result_dict = {
        "citizen_count": data['person_id'].nunique(),
        "signals_per_citizen": {
            "signal_count": counts[0].tolist(),
            "signal_sum": counts[1].tolist()
        },
        "signals_per_month" : {
            "month": list(signals_month.index),
            "sum": list(signals_month)
        }
    }
    return result_dict
