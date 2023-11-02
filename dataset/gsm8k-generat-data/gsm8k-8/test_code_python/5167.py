def solution():
    # Calculate the number of apples packed per day in week 1
    apples_per_box = 40
    boxes_per_day = 50
    apples_per_day_week1 = apples_per_box * boxes_per_day

    # Calculate the total number of apples packed in week 1 (7 days)
    total_apples_week1 = apples_per_day_week1 * 7

    # Calculate the number of apples packed per day in week 2
    apples_per_day_week2 = apples_per_day_week1 - 500

    # Calculate the total number of apples packed in week 2 (7 days)
    total_apples_week2 = apples_per_day_week2 * 7

    # Calculate the total number of apples packed in the two weeks
    total_apples_packed = total_apples_week1 + total_apples_week2
    result = total_apples_packed
    return result

print(solution())