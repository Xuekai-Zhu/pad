def solution():
    """If seven more rabbits are added to the thirteen in the cage, the number of rabbits in the cage will be 1/3 the number of rabbits Jasper saw in the park today. How many rabbits did Jasper see in the park today?"""
    # Calculate the number of rabbits in the cage after seven more are added
    rabbits_in_cage = 13 + 7

    # Calculate the number of rabbits Jasper saw in the park today
    rabbits_in_park = rabbits_in_cage * 3

    # Display the number of rabbits in the park
    result = rabbits_in_park
    return result

print(solution())