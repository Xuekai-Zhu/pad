def solution():
    
    total_ducks = 320
    eaten_on_first_night = total_ducks // 4
    remaining_after_first_night = total_ducks - eaten_on_first_night
    flown_away_on_second_night = remaining_after_first_night // 6
    remaining_after_second_night = remaining_after_first_night - flown_away_on_second_night
    stolen_on_third_night = remaining_after_second_night * 0.3
    remaining_after_three_nights = remaining_after_second_night - stolen_on_third_night
    
    return remaining_after_three_nights

print(solution())