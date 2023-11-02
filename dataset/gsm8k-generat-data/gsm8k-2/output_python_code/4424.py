def solution():
    """Mary Anne drinks 1/5 of a bottle of sparkling water every night at dinner. If each bottle costs her $2.00, how much does she spend on sparkling water every year?"""
    bottles_per_week = (1/5) * 7
    cost_per_week = bottles_per_week * 2
    cost_per_year = cost_per_week * 52
    result = cost_per_year
    return result

print(solution())