def solution():
    # Calculate the average daily distance driven by Gervais
    gervais_daily_distance = 315 / 3

    # Calculate the average daily distance driven by Henri
    henri_daily_distance = 1250 / 7

    # Calculate the difference in the average daily distance driven by Gervais and Henri
    difference = henri_daily_distance - gervais_daily_distance

    # Calculate the total difference in miles driven by Henri and Gervais over 7 days
    total_difference = difference * 7
    result = total_difference
    return result

print(solution())