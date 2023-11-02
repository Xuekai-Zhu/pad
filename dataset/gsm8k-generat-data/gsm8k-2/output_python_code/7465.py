def solution():
    """Janet pays $40/hour for 3 hours per week of clarinet lessons and $28/hour for 5 hours a week of piano lessons. How much more does she spend on piano lessons than clarinet lessons in a year?"""
    clarinet_cost = 40 * 3 * 52
    piano_cost = 28 * 5 * 52
    difference = piano_cost - clarinet_cost
    result = difference
    return result

print(solution())