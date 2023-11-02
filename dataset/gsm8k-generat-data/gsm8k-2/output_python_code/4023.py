def solution():
    """Jodi starts off walking 1 mile a day for 6 days a week. On the second week, she walks 2 miles a day, 6 days a week. On the third week, she walks 3 miles a day, 6 days a week. Finally, on the fourth week, she walks 4 miles a day, 6 days a week. How many miles has she walked in 4 weeks?"""
    week1_distance = 1 * 6
    week2_distance = 2 * 6
    week3_distance = 3 * 6
    week4_distance = 4 * 6
    total_distance = week1_distance + week2_distance + week3_distance + week4_distance
    result = total_distance
    return result

print(solution())