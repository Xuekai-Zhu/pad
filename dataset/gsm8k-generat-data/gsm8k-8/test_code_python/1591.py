def solution():
    # Define the number of yellow balloons
    yellow_balloons = 3414

    # Define the number of black balloons as 1762 more than the yellow balloons
    black_balloons = yellow_balloons + 1762

    # Calculate the total number of balloons
    total_balloons = yellow_balloons + black_balloons

    # Divide the total number of balloons evenly among 10 schools
    balloons_per_school = total_balloons / 10
    result = balloons_per_school
    return result

print(solution())