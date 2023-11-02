def solution():
    # Let's call the cost of the shirt "x"
    # Then the cost of the coat is 5x
    # We can use these equations to set up a system of equations:
    # pants + shirt = 100
    # pants + coat = 244
    # shirt + coat/5 = total_cost - pants (we know the total cost, but we don't know the individual costs yet)

    total_cost = 344  # The total cost of the pants, shirt, and coat
    pants_shirt_cost = 100  # The cost of the pants and shirt together
    pants_coat_cost = 244  # The cost of the pants and coat together

    # Solve for the cost of the shirt
    x = (pants_shirt_cost - pants_coat_cost/5) / 4

    # Solve for the cost of the coat (which is 5 times the cost of the shirt)
    coat_cost = 5*x

    result = coat_cost
    return result

print(solution())