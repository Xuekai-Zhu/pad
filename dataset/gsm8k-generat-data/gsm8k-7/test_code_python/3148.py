def solution():
    # Let x be the cost of the shirt
    # Then the cost of the coat is 5x
    # The cost of the pants is the same in both cases
    pants_and_shirt_cost = 100
    pants_and_coat_cost = 244

    # Solve the system of equations to find x and 5x
    # pants_cost + shirt_cost = 100
    # pants_cost + coat_cost = 244
    # coat_cost = 5 * shirt_cost
    shirt_cost = 28
    coat_cost = 140

    result = coat_cost
    return result

print(solution())