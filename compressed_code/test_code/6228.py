def solution():
    
    total_tomatoes = 127
    eaten_tomatoes = 19
    remaining_tomatoes = total_tomatoes - eaten_tomatoes
    given_away_tomatoes = remaining_tomatoes / 2
    tomatoes_left = remaining_tomatoes - given_away_tomatoes
    result = tomatoes_left
    return result

print(solution())