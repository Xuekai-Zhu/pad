def solution():
    basil_needed = 4
    basil_harvested = 16
    weeks_available = 8
    cups_of_pesto = (basil_harvested / basil_needed) * weeks_available
    result = cups_of_pesto
    return result

print(solution())