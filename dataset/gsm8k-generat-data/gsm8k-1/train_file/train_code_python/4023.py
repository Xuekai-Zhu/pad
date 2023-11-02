def solution():
    """Jodi starts off walking 1 mile a day for 6 days a week. On the second week, she walks 2 miles a day, 6 days a week. On the third week, she walks 3 miles a day, 6 days a week. Finally on the fourth week, she walks 4 miles a day, 6 days a week. How many miles has she walked in 4 weeks?"""
    miles_week_1 = 1 * 6
    miles_week_2 = 2 * 6
    miles_week_3 = 3 * 6
    miles_week_4 = 4 * 6
    total_miles = miles_week_1 + miles_week_2 + miles_week_3 + miles_week_4
    result = total_miles
    return result

print(solution())