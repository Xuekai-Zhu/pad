def solution():
    starting_balloons = 50
    balloons_lost = 12
    balloons_given_away = 1
    balloons_given_away_30min = 9
    balloons_from_coworker = 11

    # Calculate the total number of balloons Claire has now
    current_balloons = starting_balloons - balloons_lost - balloons_given_away + balloons_given_away_30min + balloons_from_coworker
    result = current_balloons
    return result

print(solution())