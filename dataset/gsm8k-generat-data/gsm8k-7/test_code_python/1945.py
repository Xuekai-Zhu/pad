def solution():
    max_fruit_weight = 20
    watermelon_weight = 1
    grapes_weight = 1
    oranges_weight = 1

    # Calculate the total weight of the fruits that Diego has already bought
    total_bought_weight = watermelon_weight + grapes_weight + oranges_weight

    # Calculate the remaining weight that Diego can carry in his bookbag
    remaining_weight = max_fruit_weight - total_bought_weight

    # Calculate how many pounds of apples Diego can buy
    apples_weight = remaining_weight
    result = apples_weight
    return result

print(solution())