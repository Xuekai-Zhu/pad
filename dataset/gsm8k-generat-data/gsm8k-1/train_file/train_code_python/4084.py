def solution():
    """In a forest, there are three anthills. In the first anthill, there are 100 ants, and in each next anthill, there are 20% fewer ants than in the previous one. How many ants are in the third anthill?"""
    ants_first_anthill = 100
    ants_second_anthill = ants_first_anthill - (ants_first_anthill * 0.20)
    ants_third_anthill = ants_second_anthill - (ants_second_anthill * 0.20)
    result = ants_third_anthill
    return result

print(solution())