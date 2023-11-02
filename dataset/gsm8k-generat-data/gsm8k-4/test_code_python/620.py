def solution():
    """If seven more rabbits are added to the thirteen in the cage, the number of rabbits in the cage will be 1/3 the number of rabbits Jasper saw in the park today. How many rabbits did Jasper see in the park today?"""
    
    # Define the number of rabbits in the cage and the additional rabbits
    initial_rabbits = 13
    additional_rabbits = 7
    
    # Calculate the total number of rabbits in the cage after the additional rabbits are added
    total_rabbits = initial_rabbits + additional_rabbits
    
    # Calculate the number of rabbits Jasper saw in the park, which is three times the total number in the cage
    park_rabbits = total_rabbits * 3
    
    result = park_rabbits
    return result

print(solution())