def solution():
    total_animals = 84
    raccoons = 0
    squirrels = 0

    # Set up system of equations
    # r + s = 84  (total animals)
    # r + 6s = x  (total sprayed animals)
    # solve for r (number of raccoons sprayed)

    # Multiply first equation by -1, then add equations to eliminate r
    # -r - s = -84
    # r + 6s = x
    # 5s = x - 84
    # s = (x - 84) / 5

    # Substitute s into first equation to solve for r
    # r + ((x-84)/5) = 84
    # r = 168 - x/5

    # Set up equation with known total sprayed animals
    # x = r + 6s

    # Solve for r when x = total sprayed animals
    x = total_animals
    r = 168 - x/5
    s = (x - r) / 6

    result = r
    return result

print(solution())