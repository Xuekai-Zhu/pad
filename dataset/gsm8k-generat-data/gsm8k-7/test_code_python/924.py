def solution():
    num_loads = 8
    wash_time = 0.75  # 45 minutes = 0.75 hours
    dry_time = 1

    # Calculate the total time needed to wash all loads
    total_wash_time = num_loads * wash_time

    # Calculate the total time needed to dry all loads
    total_dry_time = num_loads * dry_time

    # Calculate the total time needed to complete all laundry
    total_time = total_wash_time + total_dry_time
    result = total_time
    return result

print(solution())