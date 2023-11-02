def solution():
    ducks_initial = 320
    ducks_eaten_first_night = ducks_initial * (1/4)
    ducks_left_after_first_night = ducks_initial - ducks_eaten_first_night
    ducks_fly_away_second_night = ducks_left_after_first_night * (1/6)
    ducks_left_after_second_night = ducks_left_after_first_night - ducks_fly_away_second_night
    ducks_stolen_third_night = ducks_left_after_second_night * (3/10)
    ducks_left_after_third_night = ducks_left_after_second_night - ducks_stolen_third_night
    result = ducks_left_after_third_night
    
    return result

print(solution())