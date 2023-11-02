def solution():
    num_scoops_of_ice_cream = 2
    cost_per_scoop = 1.5
    erin_money = 6.00

    # Calculate the total cost of the ice cream scoops
    total_cost = num_scoops_of_ice_cream * cost_per_scoop

    # Calculate the number of scoops of ice cream that Erin should buy
    num_scoops_of_ice_cream = total_cost - erin_money
    result = num_scoops_of_ice_cream
    return result

print(solution())