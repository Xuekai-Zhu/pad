def solution():
    # Let's assume the number of erasers Gabriel collected is x
    x = 5

    # Celine collected twice as many erasers as Gabriel did
    celine_erasers = 2 * x

    # Julian collected twice as many erasers as Celine did
    julian_erasers = 2 * celine_erasers

    # The total number of erasers collected is 35
    total_erasers = celine_erasers + julian_erasers + x

    # Solve for x
    x = (35 - 3 * celine_erasers) / 3

    # Celine collected 2x erasers
    celine_erasers = 2 * x
    result = celine_erasers
    return result

print(solution())