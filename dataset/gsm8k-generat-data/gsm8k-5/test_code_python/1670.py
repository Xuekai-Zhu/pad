def solution():
    total_fruits = 40  # The basket holds 40 fruits
    num_apples = 3  # There are 3 times as many apples as oranges

    # Calculate the number of apples
    num_apples = total_fruits / 4  # Apples make up 3/4 of the fruits

    # Calculate the number of oranges
    num_oranges = total_fruits - num_apples

    result = num_oranges
    return result

print(solution())