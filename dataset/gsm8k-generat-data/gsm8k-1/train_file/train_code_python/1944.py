def solution():
    """Diego can carry 20 pounds of fruit home in his bookbag. If he buys a pound of watermelon, a pound of grapes, and a pound of oranges, how many pounds of apples can he buy?"""
    total_weight = 3
    weight_of_other_fruits = 3
    weight_of_apples = 20 - total_weight + weight_of_other_fruits
    result = weight_of_apples
    return result

print(solution())