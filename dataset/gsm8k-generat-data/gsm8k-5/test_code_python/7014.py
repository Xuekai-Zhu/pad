def solution():
    starting_balloons = 50  # Claire started with 50 balloons
    balloons_lost = 12  # 12 balloons floated away while she was passing them out
    balloons_given_away = 1  # Claire gave 1 balloon to a little girl
    balloons_given_away_later = 9  # She gave 9 more balloons away later
    balloons_taken_from_coworker = 11  # She took 11 balloons from her coworker

    # Calculate the total number of balloons Claire has now
    total_balloons = starting_balloons - balloons_lost - balloons_given_away + balloons_given_away_later + balloons_taken_from_coworker
    result = total_balloons
    return result

print(solution())