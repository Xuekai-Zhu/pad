def solution():
    """Susie and Britney each keep chickens, of two different breeds. Susie has 11 Rhode Island Reds and 6 Golden Comets. Britney has twice as many Rhode Island Reds as Susie, but only half as many Golden Comets. How many more chickens are in Britney's flock than in Susie's?"""
    # Define the number of chickens Susie has
    susie_rhodes = 11
    susie_comets = 6

    # Define the number of chickens Britney has
    britney_rhodes = susie_rhodes * 2
    britney_comets = susie_comets / 2

    # Calculate the total number of chickens in each flock
    susie_total = susie_rhodes + susie_comets
    britney_total = britney_rhodes + britney_comets

    # Calculate the difference in the number of chickens between the two flocks
    difference = britney_total - susie_total

    # Display the difference
    result = difference
    return result

print(solution())