def solution():
    sacks_per_harvest = 20
    increase_percentage = 0.2    # 20% increase
    num_harvests = 2

    # Calculate the total number of sacks of rice after the first harvest
    total_sacks_first_harvest = sacks_per_harvest

    # Calculate the total number of sacks of rice after the second harvest
    increase_amt = sacks_per_harvest * increase_percentage
    total_sacks_second_harvest = sacks_per_harvest + increase_amt
    total_sacks_second_harvest *= sacks_per_harvest    # Total number of sacks after second harvest

    result = (total_sacks_first_harvest, total_sacks_second_harvest)
    return result

print(solution())