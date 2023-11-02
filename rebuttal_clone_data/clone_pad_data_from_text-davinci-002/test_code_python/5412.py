def solution():
    number_of_players = 30
    water_per_player = 200
    coach_water = 8
    water_left = coach_water - (water_per_player * number_of_players) - 250
    result = water_left
    return result

print(solution())