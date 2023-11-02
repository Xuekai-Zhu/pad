def solution():
    """The population of an area starts at 100,000 people. It increases by 60% over 10 years due to birth. In that same time, 2000 people leave per year from emigration and 2500 people come in per year from immigration. How many people are in the area at the end of 10 years?"""
    population = 100000
    birth_rate = 0.6 / 10
    emigration_rate = 2000
    immigration_rate = 2500

    for i in range(10):
        population += population * birth_rate
        population += immigration_rate - emigration_rate

    result = population
    return result

print(solution())