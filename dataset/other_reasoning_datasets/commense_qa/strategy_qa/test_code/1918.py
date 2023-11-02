def solution():
    waiting_time = 14 # hours from 10am to midnight
    bladder capacity = 500 # mL
    fluids consumed = 1000 # mL
    bathroom frequency = 3 # times per day
    max bladder capacity = bladder capacity + fluids consumed - (bathroom frequency * waiting_time)
    
    if max bladder capacity < 500:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())