def solution():
    """How many girls are in the school if 40% of a school population is made up of 240 boys?"""
    boys_percentage = 40
    boys_population = 240
    total_population = (boys_population * 100) / boys_percentage
    girls_population = total_population - boys_population
    result = girls_population
    return result

print(solution())