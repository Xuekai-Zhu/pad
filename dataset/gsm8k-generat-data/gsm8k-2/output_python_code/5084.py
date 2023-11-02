def solution():
    """Salem is 15 times the size of Leesburg. Leesburg has 58940 people. If 130000 people move out of Salem, and half of Salem's population is women, how many women live in Salem?"""
    leesburg_population = 58940
    salem_population = 15 * leesburg_population - 130000
    women_population = salem_population / 2
    result = women_population
    return result

print(solution())