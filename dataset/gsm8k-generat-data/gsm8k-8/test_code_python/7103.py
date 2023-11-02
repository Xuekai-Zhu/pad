def solution():
    # Calculate the cost of buying individual balloons
    individual_balloon_cost = 0.5 * 14

    # Calculate the number of packs needed to buy 14 balloons
    num_packs = 1
    while num_packs * 10 < 14:
        num_packs += 1

    # Calculate the cost of buying packs of balloons
    pack_cost = num_packs * 3

    # Calculate the total cost
    total_cost = min(individual_balloon_cost, pack_cost)
    result = total_cost
    return result

print(solution())