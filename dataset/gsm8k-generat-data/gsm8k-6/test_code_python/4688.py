def solution():
    # Let's call the price of the coat "x"
    # The price of the shirt is then (1/3)x
    # We know that the total cost of both items is $600

    # Set up the equation:
    x + (1/3)x = 600

    # Simplify and solve for x:
    (4/3)x = 600
    x = (3/4)*600
    x = 450

    # Now we know that the coat costs $450
    # The price of the shirt is (1/3)*$450 = $150
    shirt_cost = 150
    result = shirt_cost
    return result

print(solution())