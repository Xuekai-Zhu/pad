def solution():
    # Calculate the amount of kibble the cat ate while Kira was away
    ate_kibble = 3 - 1  # the bowl had 3 pounds of kibble and there is 1 pound left
    # Calculate the number of 4-hour intervals Kira's cat ate kibble for
    intervals = ate_kibble / 1  # the cat eats 1 pound of kibble every 4 hours
    # Calculate the total number of hours Kira's cat ate kibble for
    hours_away = intervals * 4
    result = hours_away
    return result

print(solution())