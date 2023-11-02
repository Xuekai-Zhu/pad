def solution():
    # Set up equations based on the given information
    pears = apples + 2
    bananas = pears + 3
    total_fruit = apples + pears + bananas

    # Solve for the number of bananas in the bowl of fruit
    bananas = (total_fruit - 19) / 2
    result = bananas
    return result

print(solution())