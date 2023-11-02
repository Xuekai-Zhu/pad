def solution():
    klingons_in_star_trek_universe = True
    last_jedi_movie_in_star_wars_universe = True
    if klingons_in_star_trek_universe and not last_jedi_movie_in_star_wars_universe:
        result = "no"
    else:
        result = "uncertain"
    return result

print(solution())