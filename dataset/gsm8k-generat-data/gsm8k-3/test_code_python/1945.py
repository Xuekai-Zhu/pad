def solution():
    """Diego can carry 20 pounds of fruit home in his bookbag. If he buys a pound of watermelon, a pound of grapes, and a pound of oranges, how many pounds of apples can he buy?"""
    # Calculate the weight of the watermelon, grapes, and oranges
    total_weight = 3

    # Calculate the remaining weight Diego can carry
    remaining_weight = 20 - total_weight

    # Calculate the weight of one apple
    apple_weight = 0.5

    # Calculate the maximum number of apples Diego can carry
    max_apples = remaining_weight // apple_weight

    # Display the maximum number of apples Diego can carry
    result = max_apples
    return result

print(solution())