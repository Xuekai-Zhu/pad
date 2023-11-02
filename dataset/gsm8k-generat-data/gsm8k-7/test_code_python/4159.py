def solution():
    total_days = 120
    larva_time_ratio = 3

    # Calculate the total time spent in both larva and cocoon stage
    total_time = total_days / (larva_time_ratio + 1)

    # Calculate the time spent in the cocoon stage
    cocoon_time = total_time / larva_time_ratio
    result = cocoon_time
    return result

print(solution())