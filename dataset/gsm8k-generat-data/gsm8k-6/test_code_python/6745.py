def solution():
    # Calculate the initial number of balloons for each friend
    initial_balloons = 250 / 5  # evenly sharing the balloons among 5 friends
    # Calculate the number of balloons each friend has after giving Dante 11 balloons
    final_balloons = (initial_balloons - 11)
    result = final_balloons
    return result

print(solution())