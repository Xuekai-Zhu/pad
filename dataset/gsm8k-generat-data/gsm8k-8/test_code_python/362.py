def solution():
    # Set up the equations
    # Let x be the weight of Kevin's empty briefcase
    # Let y be the weight of Kevin's laptop and work papers
    # Then we have:
    # 2x = weight of Karen's tote
    # 2(x + y) = weight of Kevin's full briefcase
    # y = (1/6)(x + y)
    # We can solve for x and y using these equations

    # Start by solving for x
    x = 4  # since 2x = weight of Karen's tote and we know her tote weighs 8 pounds
    # Solve for y using the third equation
    y = (1/5) * x

    # Calculate the weight difference between Kevin's laptop and Karen's tote
    laptop_weight = 2 * y
    weight_difference = laptop_weight - 8

    result = weight_difference
    return result

print(solution())