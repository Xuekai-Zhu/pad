def solution():
    cost_per_bar = 1.5
    num_scouts = 15
    num_smores_per_bar = 3
    num_smores_per_scout = 2

    # Calculate the total number of s'mores needed
    total_smores = num_scouts * num_smores_per_scout

    # Calculate the total number of chocolate bars needed
    total_bars = total_smores / num_smores_per_bar

    # Calculate the total cost of all chocolate bars needed
    total_cost = total_bars * cost_per_bar
    result = total_cost
    return result

print(solution())