def solution():
    """In a forest, there are three anthills. In the first anthill, there are 100 ants, and in each next anthill, there are 20% fewer ants than in the previous one. How many ants are in the third anthill?"""
    # Define the number of ants in the first anthill
    ants_1 = 100

    # Calculate the number of ants in the second anthill
    ants_2 = ants_1 * 0.8

    # Calculate the number of ants in the third anthill
    ants_3 = ants_2 * 0.8

    # Display the number of ants in the third anthill
    result = ants_3
    return result

print(solution())