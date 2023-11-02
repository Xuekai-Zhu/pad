def solution():
    apples_per_box = 14  # Each box contains 14 apples
    boxes = 3  # Henry and his brother have 3 boxes of apples
    apples_per_day = 2  # Henry and his brother each eat 1 apple a day

    # Calculate the total number of apples they will eat in a week
    total_apples_per_week = apples_per_day * 7 * 2  # 2 people are eating apples

    # Calculate the total number of weeks they can spend eating the apples
    total_apples = apples_per_box * boxes
    total_weeks = total_apples // total_apples_per_week

    result = total_weeks
    return result

print(solution())