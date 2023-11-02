def solution():
    # Haylee has 3 dozen (36) guppies
    haylee_guppies = 36

    # Jose has half as many as Haylee
    jose_guppies = haylee_guppies / 2

    # Charliz has one-third of what Jose has
    charliz_guppies = jose_guppies / 3

    # Nicolai has 4 times as many as Charliz
    nicolai_guppies = charliz_guppies * 4

    # Calculate the total number of guppies
    total_guppies = haylee_guppies + jose_guppies + charliz_guppies + nicolai_guppies

    result = total_guppies
    return result

print(solution())