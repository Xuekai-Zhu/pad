def solution():
    yellow_balloons = 3414  # Number of yellow balloons
    black_balloons = yellow_balloons + 1762  # Number of black balloons
    total_balloons = yellow_balloons + black_balloons  # Total number of balloons
    schools = 10  # Number of schools to divide balloons among

    # Calculate the number of balloons each school will receive
    balloons_per_school = total_balloons / schools
    result = balloons_per_school
    return result

print(solution())