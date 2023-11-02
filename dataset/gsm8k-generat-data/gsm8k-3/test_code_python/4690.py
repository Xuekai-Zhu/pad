def solution():
    """Terry drives at a speed of 40 miles per hour. He drives daily forth and back from his home to his workplace which is 60 miles away from his home. How many hours does Terry spend driving from home to the workplace and then back?"""
    # Define the distance between Terry's home and workplace
    distance = 60

    # Calculate the time Terry spends driving to work
    time_to_work = distance / 40

    # Calculate the time Terry spends driving back home
    time_to_home = distance / 40

    # Calculate the total time Terry spends driving
    total_time = time_to_work + time_to_home

    # Display the total time Terry spends driving
    result = total_time
    return result

print(solution())