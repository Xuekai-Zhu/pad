def solution():
    """Justice has 3 ferns, 5 palms, and 7 succulent plants in her house. If she wants a total of 24 plants in her home, how many more plants does she need?"""
    ferns = 3
    palms = 5
    succulents = 7
    total_plants = ferns + palms + succulents
    plants_needed = 24 - total_plants
    result = plants_needed
    return result

print(solution())