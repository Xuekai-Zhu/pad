def solution():
    water_per_lineman = 8
    water_per_skill_player = 6
    total_water = 126
    num_linemen = 12
    num_skill_players = 10

    total_water_needed = (num_linemen * water_per_lineman) + (num_skill_players * water_per_skill_player)

    if total_water_needed <= total_water:
        result = 0
    else:
        water_needed_per_skill_player = total_water_needed - (num_linemen * water_per_lineman)
        result = water_needed_per_skill_player / water_per_skill_player

    return result

print(solution())