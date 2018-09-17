import time

def money():
    sex = 10
    while True:
        sex += 1
        time.sleep(1)
        yield sex
        
    