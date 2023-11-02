def solution():
    """Diego can carry 20 pounds of fruit home in his bookbag. If he buys a pound of watermelon, a pound of grapes, and a pound of oranges, how many pounds of apples can he buy?"""
    # Define the weight of fruit Diego has already bought
    bought_weight = 3

    # Define the maximum weight of fruit Diego can carry
    max_weight = 20

    # Calculate the weight of apples Diego can buy
    apples_weight = max_weight - bought_weight - 1 - 1 - 1

    # Return the result
    result = apples_weight
    return result

print(solution())