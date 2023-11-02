def solution():
    # Calculate the total biking time per day
    total_biking_time = 2 * 2  # Kyle bikes for 2 hours to work and back

    # Calculate the cost of one pack of snacks
    cost_per_pack = total_biking_time * 10  # Ten times the time he takes to travel to work and back

    # Calculate the cost of 50 packs of snacks
    total_cost = cost_per_pack * 50

    result = total_cost
    return result

print(solution())