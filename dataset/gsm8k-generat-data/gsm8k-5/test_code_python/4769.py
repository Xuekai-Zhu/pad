def solution():
    # Calculate the total number of episodes in the first series
    series_1_total = 12 * 16  # 12 seasons, 16 episodes per season

    # Calculate the total number of episodes in the second series
    series_2_total = 14 * 16  # 14 seasons, 16 episodes per season

    # Calculate the number of lost episodes in the first series
    series_1_lost = 2 * 12  # 2 lost episodes per season, 12 seasons

    # Calculate the number of lost episodes in the second series
    series_2_lost = 2 * 14  # 2 lost episodes per season, 14 seasons

    # Calculate the total number of remaining episodes
    total_remaining = series_1_total + series_2_total - series_1_lost - series_2_lost
    result = total_remaining
    return result

print(solution())