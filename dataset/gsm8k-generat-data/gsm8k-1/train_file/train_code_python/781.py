def solution():
    """Melissa wants to make some dresses to sell at the upcoming festival. She has 56 square meters of fabric to make them. She knows that each dress takes 4 square meters of fabric and 3 hours to make. How many hours does she have to work?"""
    fabric_available = 56
    fabric_per_dress = 4
    dresses_possible = fabric_available // fabric_per_dress
    hours_per_dress = 3
    total_hours = dresses_possible * hours_per_dress
    result = total_hours
    return result

print(solution())