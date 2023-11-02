def solution():
    """Carla can cook a batch of waffles in 10 minutes and chicken-fried steak in 6 minutes. How long will it take her to cook 3 steaks and a batch of waffles?"""
    time_waffles = 10
    time_steak = 6
    num_steaks = 3
    total_time = time_waffles + (time_steak * num_steaks)
    result = total_time
    return result

print(solution())