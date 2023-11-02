def solution():
    # Define the number of seedlings planted on the first day
    day1_planted = 200

    # Define the number of seedlings planted on the second day as twice the amount of the first day
    day2_planted = day1_planted * 2

    # Calculate the total number of seedlings planted
    total_planted = day1_planted + day2_planted

    # Calculate the number of seedlings planted by Remi's father
    father_planted = 1200 - total_planted

    result = father_planted
    return result

print(solution())