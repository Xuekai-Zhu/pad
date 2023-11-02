def solution():
    # Define the time it takes to travel from the first station to the second station
    time1 = 2

    # Define the time it takes to travel from the second station to the third station
    time2 = 2

    # Define the time Kira takes for a break at the second station
    break_time = 30/60

    # Calculate the total time Kira takes to travel from the first station to the third station
    total_time = time1 + time2 + break_time

    # Convert the total time to minutes
    total_time_in_minutes = total_time * 60

    result = total_time_in_minutes
    return result

print(solution())