def solution():
    # Set up system of equations to solve for prices of pants, shirt, and coat
    # Let p = price of pants, s = price of shirt, c = price of coat
    # p + s = 100    (pair of pants and shirt costs $100)
    # p + c = 244    (pants and coat cost $244)
    # c = 5s         (coat costs 5 times as much as shirt)

    # Solve for s using the first equation
    s = 100 - p

    # Substitute s into the second and third equations
    p + c = 244
    c = 5s

    # Substitute s back into the third equation
    c = 5(100 - p)

    # Solve for p using the second equation
    p + 5s = 244
    p + 5(100 - p) = 244
    4p = 44
    p = 11

    # Substitute p into the first and second equations to solve for s and c
    s = 100 - p
    s = 89
    c = 5s
    c = 445

    # Mr. Zubir paid $445 for his coat
    result = c
    return result

print(solution())