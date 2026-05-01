import random


#def build_headers(identity):
 #   headers = {
  #      "User-Agent": identity["user_agent"]
   # }


    #if random.choice([True, False]):
     #  headers["X-Forwarded-For"]= identity["ip"]


      # return headers
FAKE_IP_POOL = [
           f"192.168.1{i}" for i in range(2,200)
 ]



def generate_identity():
    return {

        "ip":random.choice(FAKE_IP_POOL),
        "user_agent": random.choice([
                 "Mozilla/5.0 (Windows NT 10.0)",
                 "Mozilla/5.0 (Macintosh)",
                 "Mozilla/5.0 (Linux)"
             ])

     }

def build_headers(identity):
    return {

          "User-Agent": identity["user_agent"],
          "X-Forwarded-For": identity["ip"]
     }




