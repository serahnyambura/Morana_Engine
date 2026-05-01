import json
import threading
import time

from  behaviors import baseline_user,automated_agent, threat_actor_simulator
from  safety import validate_target

stop_event = threading.Event()

def run_simulation(config):
    target = config["target"]

    validate_target(target)

    threads = []

#Baseline users
    for i in range(config["baseline_users"]):
        t = threading.Thread(target=baseline_user, args=(target, i, stop_event))
        threads.append(t)

#Automated agents
    for i in range(config["automated_agents"]):
        t = threading.Thread(target=automated_agent, args=(target, i, stop_event))
        threads.append(t)

#Threat actors
    for i in range(config["threat_actors"]):
        t = threading.Thread(target=threat_actor_simulator, args=(target, i, stop_event))
        threads.append(t)

    for t in threads:
        t.start()
    
    time.sleep(config["max_runtime"])
    stop_event.set()

    for t in  threads:
        t.join()

if __name__ == "__main__":
    with  open("config.json") as f:
        config = json.load(f)

    run_simulation(config) 



