def solution():
    """If a basket is capable of holding 40 fruit altogether, and there are 3 times as many apples as oranges, how many oranges are there?"""
    # Define the total number of fruit in the basket
    total_fruit = 40

    # Define the ratio of apples to oranges
    apple_to_orange_ratio = 3

    # Calculate the total number of oranges
    orange_count = total_fruit // (apple_to_orange_ratio + 1)

    # Display the number of oranges
    result = orange_count
    return result

print(solution())