def solution():
    # Calculate the total number of apples packed in the first week
    apples_per_box = 40
    boxes_per_day = 50
    apples_per_day = apples_per_box * boxes_per_day
    total_apples_week1 = apples_per_day * 7

    # Calculate the total number of apples packed in the second week
    apples_per_day_week2 = apples_per_day - 500
    total_apples_week2 = apples_per_day_week2 * 7

    # Calculate the total number of apples packed in both weeks
    total_apples = total_apples_week1 + total_apples_week2
    result = total_apples
    return result

print(solution())