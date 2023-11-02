def solution():
    """Celine collected twice as many erasers as Gabriel did. Julian collected twice as many erasers as Celine did. If they collected 35 erasers in total, how many erasers did Celine collect?"""
    # Let's assume Gabriel collected x erasers
    gabriel = x

    # Then Celine collected twice as many erasers as Gabriel did
    celine = 2 * gabriel

    # Julian collected twice as many erasers as Celine did
    julian = 2 * celine

    # The total number of erasers collected is 35
    total = gabriel + celine + julian

    # We can write an equation to solve for x, where x is the number of erasers Gabriel collected
    # x + 2x + 4x = 35
    # 7x = 35
    # x = 5

    # Therefore, Gabriel collected 5 erasers and Celine collected 10 erasers
    result = celine
    return result

print(solution())