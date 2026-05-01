def detect_bruteforce(events):
    return len([e for e in events if e["events"] == "login_attempt"]) > 50


def detect_scanning(events):
    pages = set([e.get("page") for e in events])
    return len(pages) > 10
 
def detect_spike(rate):
    return rate > 100
       

def detect_identity_spread(events):
    ips = set([e.get("ip") for e in events])
    return len(ips) > 30
