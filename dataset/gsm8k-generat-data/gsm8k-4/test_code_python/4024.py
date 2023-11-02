def solution():
    """Jodi starts off walking 1 mile a day for 6 days a week. On the second week, she walks 2 miles a day, 6 days a week. On the third week, she walks 3 miles a day, 6 days a week. Finally on the fourth week, she walks 4 miles a day, 6 days a week. How many miles has she walked in 4 weeks?"""
    # Define the number of days and miles for each week
    week1_days = 6
    week1_miles = 1

    week2_days = 6
    week2_miles = 2

    week3_days = 6
    week3_miles = 3

    week4_days = 6
    week4_miles = 4

    # Calculate the total number of miles walked in 4 weeks
    total_miles = (week1_days * week1_miles) + (week2_days * week2_miles) + (week3_days * week3_miles) + (week4_days * week4_miles)

    # Return the result
    result = total_miles
    return result

print(solution())