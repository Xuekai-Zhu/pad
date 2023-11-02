def solution():
    """If seven more rabbits are added to the thirteen in the cage, the number of rabbits in the cage will be 1/3 the number of rabbits Jasper saw in the park today. How many rabbits did Jasper see in the park today?"""
    rabbits_in_cage = 13
    rabbits_added = 7
    rabbits_in_cage_after_addition = rabbits_in_cage + rabbits_added
    park_rabbits = rabbits_in_cage_after_addition * 3
    
    result = park_rabbits
    
    return result

print(solution())