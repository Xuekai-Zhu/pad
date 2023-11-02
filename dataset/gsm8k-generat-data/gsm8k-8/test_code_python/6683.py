def solution():
    # Define initial counts
    apples = 10
    oranges = 5

    # Add 5 more oranges
    oranges += 5

    # Calculate total fruit count
    total_fruit = apples + oranges

    # Calculate percentage of fruit that is apples
    percentage_apples = (apples / total_fruit) * 100

    result = percentage_apples
    return result

print(solution())