def solution():
    """Haylee has 3 dozen guppies in her aquarium.  Jose has half as many guppies as Haylee in his tank.  
    Charliz has one-third of what Jose has in his tank.  Nicolai has 4 times as many guppies as Charliz in his pond. 
    How many guppies do the four friends have altogether?"""
    
    # Define the number of guppies in Haylee's aquarium
    haylee_guppies = 3 * 12

    # Define the number of guppies in Jose's tank
    jose_guppies = haylee_guppies / 2

    # Define the number of guppies in Charliz's tank
    charliz_guppies = jose_guppies / 3

    # Define the number of guppies in Nicolai's pond
    nicolai_guppies = charliz_guppies * 4

    # Calculate the total number of guppies
    total_guppies = haylee_guppies + jose_guppies + charliz_guppies + nicolai_guppies

    # Return the result
    result = total_guppies
    return result

print(solution())