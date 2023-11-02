def solution():
    """Terry drives at a speed of 40 miles per hour. He drives daily forth and back from his home to his workplace which is 60 miles away from his home. How many hours does Terry spend driving from home to the workplace and then back?"""
    # Define the distance to Terry's workplace
    DISTANCE = 60

    # Define Terry's speed
    SPEED = 40

    # Calculate the time Terry spends driving to work
    time_to_work = DISTANCE / SPEED

    # Calculate the time Terry spends driving back home
    time_back_home = DISTANCE / SPEED

    # Calculate the total time Terry spends driving each day
    total_time = time_to_work + time_back_home

    result = total_time
    return result

print(solution())