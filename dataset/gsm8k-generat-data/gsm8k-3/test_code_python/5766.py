def solution():
    """Haylee has 3 dozen guppies in her aquarium.  Jose has half as many guppies as Haylee in his tank.  Charliz has one-third of what Jose has in his tank.  Nicolai has 4 times as many guppies as Charliz in his pond. How many guppies do the four friends have altogether?"""
    # Define the number of guppies in a dozen
    GUPPIES_PER_DOZEN = 12

    # Calculate the number of guppies that Haylee has
    haylee_guppies = 3 * GUPPIES_PER_DOZEN

    # Calculate the number of guppies that Jose has
    jose_guppies = haylee_guppies / 2

    # Calculate the number of guppies that Charliz has
    charliz_guppies = jose_guppies / 3

    # Calculate the number of guppies that Nicolai has
    nicolai_guppies = charliz_guppies * 4

    # Calculate the total number of guppies that the four friends have
    total_guppies = haylee_guppies + jose_guppies + charliz_guppies + nicolai_guppies

    # Display the total number of guppies
    result = total_guppies
    return result

print(solution())