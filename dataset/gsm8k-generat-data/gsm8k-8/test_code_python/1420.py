def solution():
    # Set up the equations based on the given information
    water = x
    soda = 3*x - 6
    total = water + soda
    total = 54

    # Solve for water
    x = (total + 6) / 4
    result = x
    return result

print(solution())