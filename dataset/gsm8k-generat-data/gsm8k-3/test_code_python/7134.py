def solution():
    """Celine collected twice as many erasers as Gabriel did. Julian collected twice as many erasers as Celine did. If they collected 35 erasers in total, how many erasers did Celine collect?"""
    # Let's suppose Gabriel collected x erasers
    gabriel = x
    # Celine collected twice as many erasers as Gabriel did
    celine = 2 * gabriel
    # Julian collected twice as many erasers as Celine did
    julian = 2 * celine

    # The total number of erasers collected is 35
    total = gabriel + celine + julian
    # Let's solve for x to find how many erasers Gabriel collected
    x = (35 - julian) / 3

    # Substitute x to find how many erasers Celine collected
    celine = 2 * x
    result = celine
    return result

print(solution())