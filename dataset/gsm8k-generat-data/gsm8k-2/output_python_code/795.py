def solution():
    """Carla can cook a batch of waffles in 10 minutes and chicken-fried steak in 6 minutes. How long will it take her to cook 3 steaks and a batch of waffles?"""
    time_for_waffles = 10
    time_for_steak = 6
    num_steaks = 3
    total_time = (time_for_waffles + num_steaks * time_for_steak)
    result = total_time
    return result

print(solution())