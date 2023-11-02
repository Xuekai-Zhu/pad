def solution():
    num_bananas = 5

    # Calculate the number of oranges based on the number of bananas
    num_oranges = num_bananas * 2

    # Calculate the number of apples based on the number of oranges
    num_apples = num_oranges * 2

    # Calculate the total number of fruits on the display
    total_fruits = num_bananas + num_oranges + num_apples
    result = total_fruits
    return result

print(solution())