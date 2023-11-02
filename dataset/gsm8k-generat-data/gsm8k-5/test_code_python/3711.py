def solution():
    apples = 4
    pears = 3 * apples  # Katherine has 3 times as many pears as apples
    total_fruit = apples + pears + bananas  # Katherine has a total of 21 pieces of fruit

    # Solve for the number of bananas
    bananas = total_fruit - apples - pears
    result = bananas
    return result

print(solution())