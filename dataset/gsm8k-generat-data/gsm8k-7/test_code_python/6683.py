def solution():
    num_apples = 10
    num_oranges = 5

    # Add 5 oranges to the basket
    num_oranges += 5

    # Calculate the total number of fruit in the basket
    total_fruit = num_apples + num_oranges

    # Calculate the percentage of the fruit that is apples
    perc_apples = (num_apples / total_fruit) * 100
    result = perc_apples
    return result

print(solution())