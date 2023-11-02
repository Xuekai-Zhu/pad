def solution():
    # Calculate the ages of the dogs
    age_1st_fastest = 10
    age_2nd_fastest = age_1st_fastest - 2
    age_3rd_fastest = age_2nd_fastest + 4
    age_4th_fastest = age_3rd_fastest / 2
    age_5th_fastest = age_4th_fastest + 20

    # Calculate the average age of the 1st and 5th fastest dogs
    average_age = (age_1st_fastest + age_5th_fastest) / 2
    result = average_age
    return result

print(solution())