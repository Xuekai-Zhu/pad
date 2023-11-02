def solution():
    # Find the total number of black balloons
    black_balloons = 3414 + 1762  

    # Find the total number of balloons
    total_balloons = yellow_balloons + black_balloons

    # Find the number of balloons each school will receive
    balloons_per_school = total_balloons // 10

    result = balloons_per_school
    return result

print(solution())