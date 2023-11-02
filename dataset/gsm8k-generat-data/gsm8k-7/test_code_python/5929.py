def solution():
    num_bananas = 2
    num_apples = 2 * num_bananas
    total_fruits = 12

    # Calculate the total number of oranges in the bowl
    num_oranges = total_fruits - num_bananas - num_apples
    result = num_oranges
    return result

print(solution())