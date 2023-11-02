def solution():
    # Calculate the cost of buying individual balloons and packs of 10 balloons
    cost_of_single_balloon = 0.5
    cost_of_pack_of_10_balloons = 3
    num_packs_of_10_balloons = 1
    num_single_balloons = 4
    total_cost = (num_packs_of_10_balloons * cost_of_pack_of_10_balloons) + (num_single_balloons * cost_of_single_balloon)  # Total cost of buying balloons

    result = total_cost
    return result

print(solution())