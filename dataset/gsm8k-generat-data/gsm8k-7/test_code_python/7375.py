def solution():
    num_loads = 2
    wash_time_per_load = 45
    dry_time = 75

    # Calculate the total time for washing both loads
    total_wash_time = num_loads * wash_time_per_load

    # Calculate the total time for washing and drying both loads together
    total_time = total_wash_time + dry_time
    result = total_time
    return result

print(solution())