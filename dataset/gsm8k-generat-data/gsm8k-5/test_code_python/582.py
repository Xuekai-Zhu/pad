def solution():
    total_tomatoes = 127  # Haruto had 127 tomatoes in total
    eaten_tomatoes = 19  # Birds ate 19 of the tomatoes
    remaining_tomatoes = total_tomatoes - eaten_tomatoes  # Haruto's remaining tomatoes after the birds ate some
    given_away_tomatoes = remaining_tomatoes / 2  # Haruto gave half of his remaining tomatoes to his friend
    tomatoes_left = remaining_tomatoes - given_away_tomatoes  # Haruto's tomatoes left after giving half to his friend
    result = tomatoes_left
    return result

print(solution())