def solution():
    """Brody’s calculator can run for 60 hours on a full battery. Brody has used three quarters of its battery up, and he is about to take a two-hour math exam that will require his calculator the whole time. How many hours of battery will Brody’s calculator have left?"""
    full_battery_life = 60
    used_battery_life = full_battery_life * (3/4)
    exam_duration = 2
    remaining_battery_life = full_battery_life - used_battery_life - exam_duration
    result = remaining_battery_life
    return result

print(solution())