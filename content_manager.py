from classes.Schedule import Schedule
import json
from pathlib import Path
from typing import Dict

def load_schedule():
    #Load Json
    file_path = Path("data/schedule.json")
    with file_path.open("r",encoding="utf-8") as f:
        raw_data= json.load(f)

    schedule_map: Dict[str, Schedule] ={}

    #Parse each json object into a Schedule instead
    schedule_map= {key: Schedule(**schedule_data) for key,schedule_data in raw_data.items()}
    
    print("Loading Schedule")
    for k,s in schedule_map.items():
        print(f"{s.time} - {s.caption} on {s.platform}")
    return schedule_map