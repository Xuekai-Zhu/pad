def solution():
    elizabeth_ii_became_queen_year = 1952
    persian_gulf_war_start_year = 1990
    persian_gulf_war_end_year = 1991
    if elizabeth_ii_became_queen_year <= persian_gulf_war_start_year and elizabeth_ii_became_queen_year <= persian_gulf_war_end_year:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())