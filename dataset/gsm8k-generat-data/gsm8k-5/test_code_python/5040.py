def solution():
    total_ducks = 320  # There are 320 ducks in the pond
    ducks_eaten_first_night = total_ducks // 4  # 1/4 of the ducks get eaten on the first night
    remaining_ducks = total_ducks - ducks_eaten_first_night  # Remaining ducks after first night
    ducks_fly_away_second_night = remaining_ducks // 6  # 1/6 of the remaining ducks fly away on the second night
    remaining_ducks -= ducks_fly_away_second_night  # Remaining ducks after second night
    ducks_stolen_third_night = int(0.3 * remaining_ducks)  # 30% of the remaining ducks are stolen on the third night
    remaining_ducks -= ducks_stolen_third_night  # Remaining ducks after third night
    result = remaining_ducks
    return result

print(solution())