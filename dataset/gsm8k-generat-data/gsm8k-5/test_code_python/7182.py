def solution():
    # Let x be the original number
    # Double the number and add 5 to the result
    expr1 = 2*x + 5
    # Half of the original number plus 20
    expr2 = 0.5*x + 20
    # Set the two expressions equal to each other
    equation = expr1 - expr2
    # Solve for x
    x = equation / 1.5  # Divide both sides by 1.5
    result = x
    return result

print(solution())