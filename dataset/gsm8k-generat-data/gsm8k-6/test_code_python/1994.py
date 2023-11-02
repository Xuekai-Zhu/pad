def solution():
    # Calculate the number of oranges that Tom sold
    oranges_sold = 40 * (1/4)

    # Calculate the number of apples that Tom sold
    apples_sold = 70 * (1/2)

    # Calculate the number of fruits that were left
    remaining_fruits = 40 + 70 - oranges_sold - apples_sold
    result = remaining_fruits
    return result

print(solution())