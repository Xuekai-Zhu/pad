def solution():
    # Calculate the total weight of fruit that can fit in 3 bags
    total_weight = 49 * 3

    # Calculate the weight of each type of fruit needed to fill 3 bags
    apples_weight = ((4 + 3) / 2) * (total_weight / (4 + 3))
    # 4 and 3 are the weights of an apple and an orange, respectively. 
    # We take their average to get the weight per piece of fruit, and multiply it by the total number of fruits needed to fill 3 bags.

    # Calculate the weight of apples needed to fill 3 bags
    apples_required = apples_weight / 4

    result = apples_required
    return result

print(solution())