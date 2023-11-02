def solution():
    total_tomatoes = 127
    eaten_tomatoes = 19
    picked_tomatoes = total_tomatoes - eaten_tomatoes

    # Calculate the number of tomatoes Haruto gave to his friend
    tomatoes_given_away = picked_tomatoes / 2

    # Calculate the number of tomatoes Haruto has left
    tomatoes_left = picked_tomatoes - tomatoes_given_away
    result = tomatoes_left
    return result

print(solution())