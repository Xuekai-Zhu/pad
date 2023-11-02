def solution():
    acres_of_farmland = 55  # Steven has 55 acres of farmland to plow
    acres_of_grassland = 30  # Steven has 30 acres of grassland to mow
    plowing_speed = 10  # Steven can plow up to 10 acres of farmland per day
    mowing_speed = 12  # Steven can mow up to 12 acres of grassland per day

    # Calculate the time it will take Steven to plow his farmland
    time_to_plow = acres_of_farmland / plowing_speed

    # Calculate the time it will take Steven to mow his grassland
    time_to_mow = acres_of_grassland / mowing_speed

    # Calculate the total time it will take Steven to plow his farmland and mow his grassland
    total_time = time_to_plow + time_to_mow
    result = total_time
    return result

print(solution())