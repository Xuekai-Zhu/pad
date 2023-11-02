def solution():
    day1_planted = 200
    day2_planted = 2 * day1_planted
    total_planted = day1_planted + day2_planted
    total_transferred = 1200

    # Calculate the number of seedlings Remi planted on day 2
    remi_day2_planted = total_transferred - day1_planted

    # Calculate the number of seedlings Remi's father planted
    father_planted = total_planted - remi_day2_planted
    result = father_planted
    return result

print(solution())