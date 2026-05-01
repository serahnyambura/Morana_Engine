import json
import time

LOG_FILE = "logs/morana.json"

 
def log(event):
    event["timestamp"] = time.time()
   
    with open(LOG_FILE, "a") as f:
         f.write(json.dumps(event) + "\n")

    




