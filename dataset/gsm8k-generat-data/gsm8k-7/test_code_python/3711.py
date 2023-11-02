def solution():
    num_apples = 4
    num_pears = 3 * num_apples
    total_fruit = 21

    # Calculate the total number of bananas
    num_bananas = total_fruit - num_apples - num_pears
    result = num_bananas
    return result

print(solution())