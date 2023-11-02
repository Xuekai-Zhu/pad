def solution():
    """Julio makes a mocktail every evening. He uses 1 tablespoon of lime juice and tops with 1 cup of sparkling water. He can usually squeeze 2 tablespoons of lime juice per lime. After 30 days, if limes are 3 for $1.00, how much will he have spent on limes?"""
    limes_per_mocktail = 0.5
    mocktails_per_day = 1
    days = 30
    limes_per_day = limes_per_mocktail * mocktails_per_day
    limes_needed = limes_per_day * days
    total_cost = (limes_needed // 3 + 1) * 1
    result = total_cost
    return result

print(solution())