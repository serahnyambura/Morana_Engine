import time
import requests
from traffic_identity import generate_identity, build_headers

def request_with_identity(method, url, retries=3 , delay=0.5, **kwargs):
    
    for attempt in range(retries):
        try:
            identity = generate_identity() 

            headers = build_headers(identity)
            
            kwargs["headers"] = headers
            
            response = requests.request(method,url,timeout=3, **kwargs)

            return response, identity
              
        except Exception as e:
             time.sleep(delay * (attempt + 1))

    return None, identity








