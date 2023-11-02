def solution():
    iron_man_survives_infinity_war = False
    iron_man_uses_stones_in_endgame = True
    iron_man_dies_after_using_stones = True
    if iron_man_uses_stones_in_endgame and not iron_man_dies_after_using_stones:
        iron_man_survives_infinity_war = True
    return iron_man_survives_infinity_war

print(solution())