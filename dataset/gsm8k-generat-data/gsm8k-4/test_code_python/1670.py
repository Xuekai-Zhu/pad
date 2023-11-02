def solution():
    """If a basket is capable of holding 40 fruit altogether, and there are 3 times as many apples as oranges, how many oranges are there?"""
    # Define the total number of fruits and the ratio of apples to oranges
    total_fruits = 40
    apple_to_orange_ratio = 3

    # Calculate the total number of oranges
    total_oranges = total_fruits / (apple_to_orange_ratio + 1)

    # Calculate the number of apples
    total_apples = total_oranges * apple_to_orange_ratio

    # Display the number of oranges
    result = total_oranges
    return result

print(solution())