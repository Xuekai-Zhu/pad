def solution():
    """Cheryl needs 4 cups of basil to make 1 cup of pesto. She can harvest 16 cups of basil from her farm every week for 8 weeks. How many cups of pesto will she be able to make?"""
    basil_per_cup = 4
    basil_harvest_per_week = 16
    weeks = 8
    total_basil_harvested = basil_harvest_per_week * weeks
    cups_of_pesto = total_basil_harvested // basil_per_cup
    result = cups_of_pesto
    return result

print(solution())