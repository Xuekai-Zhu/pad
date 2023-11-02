def solution():
    # Calculate the time it takes Julia to run 5 miles in her old shoes
    old_shoes_time = 5 * 10  # Julia can run 1 mile in 10 minutes, so she can run 5 miles in 50 minutes

    # Calculate the time it takes Julia to run 5 miles in her new shoes
    new_shoes_time = 5 * 13  # Julia takes 13 minutes to run 1 mile, so she takes 65 minutes to run 5 miles

    # Calculate the difference in time
    time_difference = new_shoes_time - old_shoes_time
    result = time_difference
    return result

print(solution())