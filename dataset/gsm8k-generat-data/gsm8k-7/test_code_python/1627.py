def solution():
    first_hose_rate = 50
    second_hose_rate = 70
    wait_time = 3
    additional_time = 2

    # Calculate the total amount of water filled by the first hose
    first_hose_water = first_hose_rate * wait_time

    # Calculate the remaining amount of water needed to fill the pool
    remaining_water = first_hose_water - pool_capacity

    # Calculate the combined rate of both hoses
    combined_rate = first_hose_rate + second_hose_rate

    # Calculate the amount of water filled by both hoses in the additional time
    additional_water = combined_rate * additional_time

    # Calculate the total amount of water filled by both hoses
    total_water = first_hose_water + additional_water

    # Calculate the capacity of Grace's pool
    pool_capacity = total_water / 2
    result = pool_capacity
    return result

print(solution())