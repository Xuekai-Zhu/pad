def solution():
    """Susie and Britney each keep chickens, of two different breeds. Susie has 11 Rhode Island Reds and 6 Golden Comets. Britney has twice as many Rhode Island Reds as Susie, but only half as many Golden Comets. How many more chickens are in Britney's flock than in Susie's?"""
    susie_rhode_reds = 11
    susie_golden_comets = 6
    britney_rhode_reds = susie_rhode_reds * 2
    britney_golden_comets = susie_golden_comets / 2
    susie_total_chickens = susie_rhode_reds + susie_golden_comets
    britney_total_chickens = britney_rhode_reds + britney_golden_comets
    difference = britney_total_chickens - susie_total_chickens
    result = difference
    return result

print(solution())