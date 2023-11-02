def solution():
    yellow_balloons = 3414
    black_balloons = yellow_balloons + 1762
    total_balloons = yellow_balloons + black_balloons
    num_schools = 10

    # Calculate the number of balloons each school will receive
    balloons_per_school = total_balloons / num_schools
    result = balloons_per_school
    return result

print(solution())