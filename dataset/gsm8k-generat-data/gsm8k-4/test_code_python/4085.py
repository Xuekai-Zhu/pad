def solution():
    """In a forest, there are three anthills. In the first anthill, there are 100 ants, and in each next anthill, there are 20% fewer ants than in the previous one. How many ants are in the third anthill?"""
    # Define the number of ants in the first anthill
    ants_first_anthill = 100

    # Calculate the number of ants in the second anthill
    ants_second_anthill = ants_first_anthill * 0.8

    # Calculate the number of ants in the third anthill
    ants_third_anthill = ants_second_anthill * 0.8

    result = ants_third_anthill
    return result

print(solution())