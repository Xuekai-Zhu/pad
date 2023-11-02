def solution():
    num_apples_1st_weeks = 14
    num_apples_2nd_weeks = 2*num_apples_1st_weeks
    num_apples_3rd_weeks = 21
    num_total_weeks = 7
    total_apples = num_apples_1st_weeks + num_apples_2nd_weeks + num_apples_3rd_weeks
    avg_apples_per_week = total_apples / num_total_weeks
    result = avg_apples_per_week
    return result

print(solution())