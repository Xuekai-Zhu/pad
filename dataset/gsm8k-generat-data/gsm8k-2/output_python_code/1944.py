def solution():
    """Diego can carry 20 pounds of fruit home in his bookbag. If he buys a pound of watermelon, a pound of grapes, and a pound of oranges, how many pounds of apples can he buy?"""
    max_fruit_weight = 20
    current_fruit_weight = 3  # watermelon, grapes, and oranges
    available_weight = max_fruit_weight - current_fruit_weight
    apple_weight = available_weight

    result = apple_weight
    return result

print(solution())