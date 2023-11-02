def solution():
    """There are 320 ducks in a pond. On the first night 1/4 of them get eaten by a fox. On the second night 1/6 of the remaining ducks fly away, and on the third night 30 percent are stolen. How many ducks remain after the three nights?"""
    total_ducks = 320
    eaten_on_first_night = total_ducks // 4
    remaining_after_first_night = total_ducks - eaten_on_first_night
    flown_away_on_second_night = remaining_after_first_night // 6
    remaining_after_second_night = remaining_after_first_night - flown_away_on_second_night
    stolen_on_third_night = remaining_after_second_night * 0.3
    remaining_after_three_nights = remaining_after_second_night - stolen_on_third_night
    
    return remaining_after_three_nights

print(solution())