def solution():
    # Calculate the volume of the pool
    volume = 10 * 8 * 6

    # Calculate the number of quarts of chlorine needed
    chlorine_quarts = volume / 120

    # Calculate the total cost of the chlorine
    chlorine_cost = chlorine_quarts * 3

    result = chlorine_cost
    return result

print(solution())