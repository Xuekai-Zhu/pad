def solution():
    time_assembling = 1.0
    time_baking = 1.5 * 2  # doubled due to oven failure
    time_decorating = 1.0
    total_time = time_assembling + time_baking + time_decorating
    result = total_time
    return result

print(solution())