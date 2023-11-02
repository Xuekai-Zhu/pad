def solution():
    peaches_per_dozen = 12  # There are 12 peaches in a dozen
    total_peaches = 5 * peaches_per_dozen  # Susan bought 5 dozens of peaches
    bags = 2  # Susan brought 2 cloth bags
    knapsack_peaches = total_peaches / (2 * bags + 1)  # Half as many peaches as in each cloth bag

    result = knapsack_peaches
    return result

print(solution())