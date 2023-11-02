def solution():
    total_kids = 40
    tubers_percent = 0.25  # 1/4
    rafters_percent = 0.5  # 1/2

    # Calculate the number of kids who went tubing
    num_tubers = total_kids * tubers_percent

    # Calculate the number of kids who went rafting
    num_rafters = num_tubers * rafters_percent

    result = num_rafters
    return result

print(solution())