def solution():
    """Rozanne is making eggnog for her family. She uses 4 dozen eggs that were in cases and another 2 eggs that were loose in the cupboard. She puts out trays that each hold 5 glasses of eggnog. If each glass needs 5 eggs, how many trays can Rozanne put out?"""
    eggs_in_cases = 4 * 12
    eggs_loose = 2
    total_eggs = eggs_in_cases + eggs_loose
    glasses_per_tray = 5
    eggs_per_glass = 5
    total_glasses = total_eggs // eggs_per_glass
    trays = total_glasses // glasses_per_tray
    result = trays
    return result

print(solution())