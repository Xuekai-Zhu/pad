def solution():
    is_star_wars_widely_parodied = True
    is_star_wars_merchandise_plentiful = True
    is_darth_vader_a_character_in_star_wars = True
    if is_star_wars_widely_parodied or is_star_wars_merchandise_plentiful or is_darth_vader_a_character_in_star_wars:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())