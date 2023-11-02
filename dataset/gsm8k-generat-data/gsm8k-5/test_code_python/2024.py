def solution():
    red_balloons = 20 - 3  # 3 red balloons burst before the party started
    green_balloons = 15 - 2  # 2 green balloons burst before the party started

    # Calculate the total number of balloons left
    total_balloons = red_balloons + green_balloons
    result = total_balloons
    return result

print(solution())