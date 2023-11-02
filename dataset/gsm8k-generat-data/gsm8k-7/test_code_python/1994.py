def solution():
    num_oranges = 40
    num_apples = 70

    # Calculate the number of oranges sold
    sold_oranges = num_oranges / 4

    # Calculate the number of apples sold
    sold_apples = num_apples / 2

    # Calculate the total number of fruits remaining
    fruits_remaining = num_oranges - sold_oranges + num_apples - sold_apples
    result = fruits_remaining
    return result

print(solution())