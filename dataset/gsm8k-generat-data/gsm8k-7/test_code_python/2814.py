def solution():
    wait_time = 3 + 13 + 14 + 18  # total wait time in minutes
    total_time = 90  # total shopping time in minutes

    # Calculate the time spent shopping by subtracting the wait time from the total time
    shopping_time = total_time - wait_time
    result = shopping_time
    return result

print(solution())