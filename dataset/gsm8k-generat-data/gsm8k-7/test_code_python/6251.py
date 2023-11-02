def solution():
    num_peaches = 5 * 12
    num_bags = 2

    # Calculate the number of peaches she put in each cloth bag
    num_peaches_per_bag = num_peaches / num_bags

    # Calculate the number of peaches she put in the knapsack
    num_peaches_in_knapsack = num_peaches_per_bag / 2
    result = num_peaches_in_knapsack
    return result

print(solution())