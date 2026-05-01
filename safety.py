ALLOWED_TARGETS = ["http://localhost", "http://127.0.0.1","http://192.168.1.61" ]

def validate_target(target):
    if not any(target.startswith(t) for t in ALLOWED_TARGETS):
       raise Exception("Target not allowed.Lab use only.")




