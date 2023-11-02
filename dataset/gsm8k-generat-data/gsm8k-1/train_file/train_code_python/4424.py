def solution():
    """Mary Anne drinks 1/5 of a bottle of sparkling water every night at dinner. If each bottle costs her $2.00, how much does she spend on sparkling water every year?"""
    bottles_per_night = 1/5
    cost_per_bottle = 2
    nights_per_year = 365
    total_cost = bottles_per_night * nights_per_year * cost_per_bottle
    result = total_cost
    return result

print(solution())