def solution():
    """In a forest, there are three anthills. In the first anthill, there are 100 ants, and in each next anthill, there are 20% fewer ants than in the previous one. How many ants are in the third anthill?"""
    first_anthill_ants = 100
    second_anthill_ants = first_anthill_ants * 0.8
    third_anthill_ants = second_anthill_ants * 0.8
    result = third_anthill_ants
    return result

print(solution())