def solution():
    """Susie and Britney each keep chickens, of two different breeds. Susie has 11 Rhode Island Reds and 6 Golden Comets. Britney has twice as many Rhode Island Reds as Susie, but only half as many Golden Comets. How many more chickens are in Britney's flock than in Susie's?"""
    susie_rhodes = 11
    susie_golden = 6
    britney_rhodes = 2 * susie_rhodes
    britney_golden = susie_golden / 2
    susie_total = susie_rhodes + susie_golden
    britney_total = britney_rhodes + britney_golden
    difference = britney_total - susie_total
    result = difference
    return result

print(solution())