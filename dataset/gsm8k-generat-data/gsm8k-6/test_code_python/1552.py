def solution():
    # Let's assume there are x men and y women
    # We know that x + y = 180 (total number of employees)
    # We also know that x = y - 20 (20 fewer men than women)

    # Solving for y, we get y = 100
    y = 180 / 2  # since the total number of employees is 180 and we assume an equal number of men and women
    x = y - 20

    result = x
    return result

print(solution())