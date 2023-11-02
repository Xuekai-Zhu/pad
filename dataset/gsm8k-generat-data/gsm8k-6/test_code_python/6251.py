def solution():
    total_peaches = 5*12  # Susan buys five dozen peaches
    bags_peaches = total_peaches / 2  # Susan divides the peaches into two identical cloth bags
    knapsack_peaches = bags_peaches / 2  # Susan puts half as many peaches in the knapsack as in each cloth bag
    result = knapsack_peaches
    return result

print(solution())