def solution():
    # Calculate the time it takes to fill one barrel with leak
    leak_time = 5  # minutes to fill one barrel with leak

    # Calculate the time it takes to fill one barrel normally
    normal_time = 3  # minutes to fill one barrel normally

    # Calculate the extra time it takes to fill one barrel with leak
    extra_time = leak_time - normal_time

    # Calculate the total extra time it takes to fill 12 barrels with leak
    total_extra_time = extra_time * 12

    result = total_extra_time
    return result

print(solution())