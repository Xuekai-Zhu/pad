def solution():
    # Calculate the total number of peaches Susan bought
    total_peaches = 5 * 12

    # Calculate the number of peaches in each cloth bag
    peaches_per_bag = total_peaches / 2

    # Calculate the number of peaches in the knapsack
    knapsack_peaches = peaches_per_bag / 2

    result = knapsack_peaches
    return result

print(solution())