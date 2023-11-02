def solution():
    """Brody’s calculator can run for 60 hours on a full battery. Brody has used three quarters of its battery up, 
    and he is about to take a two-hour math exam that will require his calculator the whole time. 
    How many hours of battery will Brody’s calculator have left?"""
    full_battery = 60
    used_battery = full_battery * 0.75
    remaining_battery = used_battery - 2
    result = remaining_battery
    return result

print(solution())