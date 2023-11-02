def solution():
    """5,000 people live in a small town. 2,000 males live in that town and the rest of the population are females. Thirty percent of the female population wears glasses. How many females wear glasses?"""
    total_population = 5000
    male_population = 2000
    female_population = total_population - male_population
    females_with_glasses = int(0.3 * female_population)
    result = females_with_glasses
    return result

print(solution())