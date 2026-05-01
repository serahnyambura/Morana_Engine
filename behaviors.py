import time
import random
from  utils import request_with_identity
from logger import log



def baseline_user(target, user_id, stop_event):
    while not stop_event.is_set():
          res, identity = request_with_identity("GET", target + "/")

          
          log({

                 "event": "page_visit",
                 "actor": "baseline_user",
                 "user_id":user_id,
                 "ip": identity["ip"] if identity else "unknown",
                 "user_agent": identity["user_agent"] if identity else "unknown"
                 
                })

          time.sleep(random.uniform(1,5))

def automated_agent(target, agent_id, stop_event):

    while not stop_event.is_set():
          res, identity = request_with_identity("GET",target + "/products.html")

          

          log({

                  "event": "automated_access",
                  "actor": "automation",
                  "agent_id": agent_id,
                  "ip": identity["ip"] if identity else"unknown",
                  "user_agent": identity["user_agent"]if identity else "unknown"

                 })

          time.sleep(random.uniform(0.05,0.3))

def threat_actor_simulator(target, actor_id, stop_event):

    while not stop_event.is_set():
          res, identity = request_with_identity(
          
               "POST",
                  target + "/login.html",
                  data={"username": "admin", "password": "test"}
                )                
          
                

          log({

                  "event": "login_attempt",
                  "actor": "threat_simulator",
                  "actor_id": actor_id,
                  "status": "failed",
                  "ip": identity["ip"] if identity else "unknown",
                  "user_agent": identity["user_agent"] if identity else "unknown"

                 })

          time.sleep(random.uniform(0.2,1))




