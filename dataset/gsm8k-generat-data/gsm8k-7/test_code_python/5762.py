def solution():
    num_kinder = 26
    num_first = 19
    num_second = 20
    num_third = 25
    time_per_check = 2  # minutes per check

    # Calculate the total number of checks the nurse must conduct
    total_checks = num_kinder + num_first + num_second + num_third

    # Calculate the total time it will take in minutes
    total_time = total_checks * time_per_check

    # Convert to hours
    total_time_hours = total_time / 60

    result = total_time_hours
    return result

print(solution())