def solution():
    """Janet pays $40/hour for 3 hours per week of clarinet lessons and $28/hour for 5 hours a week of piano lessons. How much more does she spend on piano lessons than clarinet lessons in a year?"""
    clarinet_rate = 40
    piano_rate = 28
    clarinet_hours = 3
    piano_hours = 5
    weeks_per_year = 52
    clarinet_cost = clarinet_rate * clarinet_hours * weeks_per_year
    piano_cost = piano_rate * piano_hours * weeks_per_year
    difference = piano_cost - clarinet_cost
    result = difference
    return result

print(solution())