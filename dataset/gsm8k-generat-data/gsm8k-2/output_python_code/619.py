def solution():
    """If seven more rabbits are added to the thirteen in the cage, the number of rabbits in the cage will be 1/3 the number of rabbits Jasper saw in the park today. How many rabbits did Jasper see in the park today?"""
    cage_rabbits = 13
    park_rabbits = (cage_rabbits + 7) * 3
    result = park_rabbits
    return result

print(solution())