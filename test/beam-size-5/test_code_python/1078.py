def solution():
    # Calculate the time it took James to walk to the store
    time_to_store = 4 / 4  # James walks 4 miles per hour at home

    # Calculate the time it took James to walk back
    time_back = time_to_store / 2  # James walks halfway at home

    # Calculate the total time it took James to reach the store
    total_time = time_to_store + time_back
    result = total_time
    return result

print(solution())