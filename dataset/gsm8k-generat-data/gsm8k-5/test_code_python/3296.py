def solution():
    time_to_work_and_back = 2 * 2  # Kyle spends 2 hours biking to work and 2 hours biking back
    cost_per_times = time_to_work_and_back / 10  # The cost of each pack of snacks is 1/10 of the time to work and back
    packs_of_snacks = 50  # Kyle wants to buy 50 packs of snacks

    # Calculate the total cost of the snacks
    total_cost = cost_per_times * packs_of_snacks
    result = total_cost
    return result

print(solution())