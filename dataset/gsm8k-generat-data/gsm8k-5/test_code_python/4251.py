def solution():
    week1_distance = 2  # Carly runs 2 miles in the first week
    week2_distance = week1_distance * 2 + 3  # Carly runs twice as long as the first week plus 3 extra miles in the second week
    week3_distance = week2_distance * (9/7)  # Carly runs 9/7 as much as she ran in the second week in the third week
    week4_distance = week3_distance - 5  # Carly reduces her running time by 5 miles in the fourth week due to injury

    result = week4_distance
    return result

print(solution())