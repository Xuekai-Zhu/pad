def solution():
    # Calculate the total amount of time Jason spends shooting flames every minute
    flame_time = 5 / 15  # Jason shoots flames for every 15 seconds
    result = flame_time * 60  # multiply by 60 to get seconds per minute
    return result

print(solution())