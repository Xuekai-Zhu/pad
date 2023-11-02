def solution():
    """Susie and Britney each keep chickens, of two different breeds. Susie has 11 Rhode Island Reds and 6 Golden Comets. Britney has twice as many Rhode Island Reds as Susie, but only half as many Golden Comets. How many more chickens are in Britney's flock than in Susie's?"""
    # Define the number of Rhode Island Reds and Golden Comets for Susie
    susie_reds = 11
    susie_comets = 6

    # Calculate the number of Rhode Island Reds and Golden Comets for Britney
    britney_reds = susie_reds * 2
    britney_comets = susie_comets / 2

    # Calculate the total number of chickens for Susie and Britney
    susie_total = susie_reds + susie_comets
    britney_total = britney_reds + britney_comets

    # Calculate the difference in the number of chickens between Susie and Britney
    difference = britney_total - susie_total

    # return the result
    result = difference
    return result

print(solution())