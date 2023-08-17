import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_person(number_of_records:int):
    subtractionDays = np.random.randint(1,365)
    startDate = (datetime.today() - timedelta(days=subtractionDays)).date()
    addition_days_since_start = np.random.randint(1,subtractionDays, size=number_of_records)
    
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