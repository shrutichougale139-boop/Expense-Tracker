import datetime

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Running: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Completed: {func.__name__}\n")
        return result
    return wrapper

def get_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")
              