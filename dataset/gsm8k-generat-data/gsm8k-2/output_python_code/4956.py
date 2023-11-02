def solution():
    """Jan enters a double dutch competition. After training she doubles her speed which used to be 70 skips per minute. How many skips does she do in 5 minutes?"""
    starting_speed = 70
    new_speed = 2 * starting_speed
    time = 5
    total_skips = new_speed * time
    result = total_skips
    return result

print(solution())