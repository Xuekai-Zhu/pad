def solution():
    haylee_guppies = 3 * 12  # Haylee has 3 dozen (36) guppies
    jose_guppies = haylee_guppies / 2  # Jose has half as many guppies as Haylee
    charliz_guppies = jose_guppies / 3  # Charliz has one-third of what Jose has
    nicolai_guppies = charliz_guppies * 4  # Nicolai has 4 times as many guppies as Charliz

    # Calculate the total number of guppies the four friends have altogether
    total_guppies = haylee_guppies + jose_guppies + charliz_guppies + nicolai_guppies
    result = total_guppies
    return result

print(solution())