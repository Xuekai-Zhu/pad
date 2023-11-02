def solution():
    apples_per_box = 40
    boxes_per_day = 50
    normal_apples_per_day = apples_per_box * boxes_per_day
    normal_weekly_total = normal_apples_per_day * 7
    reduced_apples_per_day = normal_apples_per_day - 500
    reduced_weekly_total = reduced_apples_per_day * 7
    total_apples_packed = normal_weekly_total + reduced_weekly_total
    result = total_apples_packed
    return result

print(solution())