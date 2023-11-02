def solution():
    sean_played = 50 * 14  # Sean played for 50 minutes a day for 14 days
    total_played = 1512  # Sean and Indira played cricket for a total of 1512 minutes
    indira_played = total_played - sean_played  # Indira played cricket for the remaining time

    result = indira_played
    return result

print(solution())