def solution():
    num_days = 30
    num_apples_picked_per_day = 4
    remaining_apples = 230

    # Calculate the total number of apples picked in the first 30 days
    total_apples_in_30_days = num_days * num_apples_picked_per_day

    # Calculate the total number of apples collected from the orchard
    total_apples_collected = total_apples_in_30_days + remaining_apples
    result = total_apples_collected
    return result

print(solution())