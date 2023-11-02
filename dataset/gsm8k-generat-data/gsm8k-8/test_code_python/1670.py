def solution():
    # Define the ratio of apples to oranges
    apple_to_orange_ratio = 3

    # Define the total number of fruits
    total_fruits = 40

    # Calculate the total number of oranges
    orange_count = total_fruits / (apple_to_orange_ratio + 1)

    result = orange_count
    return result

print(solution())