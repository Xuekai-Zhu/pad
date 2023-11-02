def solution():
    # Calculate the amount of kibble her cat has eaten
    eaten_kibble = 3 - 1  # Kira's cat ate 2 pounds of kibble

    # Calculate the number of 4-hour intervals Kira was away from home
    intervals = eaten_kibble / 1  # Kira's cat eats 1 pound of kibble every 4 hours, so 2 pounds in 8 hours

    # Calculate the total time Kira was away from home
    hours_away = intervals * 4
    result = hours_away
    return result

print(solution())