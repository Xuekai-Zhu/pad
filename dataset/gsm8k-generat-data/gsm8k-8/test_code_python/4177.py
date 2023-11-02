def solution():
    # Set up the equations based on the given information
    # Let x be the weight of the chihuahua in pounds
    # Then the pitbull weighs 3x pounds, and the great dane weighs 3(3x) + 10 pounds
    # The sum of their weights is 439 pounds
    x = symbols('x')
    eq1 = x + 3*x + (3*3*x + 10) - 439

    # Solve for x to find the weight of the chihuahua
    x_val = solve(eq1, x)

    # Calculate the weight of the great dane
    great_dane_weight = 3*3*x_val[0] + 10
    result = great_dane_weight
    return result

print(solution())