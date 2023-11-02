def solution():
    """Haylee has 3 dozen guppies in her aquarium. Jose has half as many guppies as Haylee in his tank. Charliz has one-third of what Jose has in his tank. Nicolai has 4 times as many guppies as Charliz in his pond. How many guppies do the four friends have altogether?"""
    haylee_guppies = 3 * 12
    jose_guppies = haylee_guppies / 2
    charliz_guppies = jose_guppies / 3
    nicolai_guppies = charliz_guppies * 4
    total_guppies = haylee_guppies + jose_guppies + charliz_guppies + nicolai_guppies
    result = total_guppies
    return result

print(solution())