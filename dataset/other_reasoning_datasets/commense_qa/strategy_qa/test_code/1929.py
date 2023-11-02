def solution():
    al_pacino_birth_year = 1940
    world_war_ii_start_year = 1939
    world_war_ii_end_year = 1945
    al_pacino_first_movie_year = 1969
    if al_pacino_birth_year >= world_war_ii_start_year and al_pacino_birth_year <= world_war_ii_end_year:
        result = "no"
    elif al_pacino_first_movie_year >= world_war_ii_start_year and al_pacino_first_movie_year <= world_war_ii_end_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())