def solution():
    saving_private_ryan_year = 1998
    war_horse_year = 2011
    world_war_ii_start = 1939
    world_war_i_end = 1918
    if saving_private_ryan_year > war_horse_year and saving_private_ryan_year > world_war_ii_start and war_horse_year < world_war_i_end:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())