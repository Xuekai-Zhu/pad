def solution():
    
    total_distance = 30
    jesse_distance_first_3_days = (2/3) * 3
    jesse_distance_day_4 = 10
    mia_distance_first_4_days = 3 * 4
    jesse_distance_last_3_days = total_distance - jesse_distance_first_3_days - jesse_distance_day_4
    mia_distance_last_3_days = total_distance - mia_distance_first_4_days

    jesse_average = jesse_distance_last_3_days / 3
    mia_average = mia_distance_last_3_days / 3

    average_of_averages = (jesse_average + mia_average) / 2

    result = average_of_averages
    return result

print(solution())