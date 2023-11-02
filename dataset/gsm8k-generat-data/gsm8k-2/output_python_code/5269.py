def solution():
    """Cheryl needs 4 cups of basil to make 1 cup of pesto. She can harvest 16 cups of basil from her farm every week for 8 weeks. How many cups of pesto will she be able to make?"""
    basil_for_pesto = 4
    harvested_basil = 16 * 8
    cups_of_pesto = harvested_basil // basil_for_pesto
    result = cups_of_pesto
    return result

print(solution())