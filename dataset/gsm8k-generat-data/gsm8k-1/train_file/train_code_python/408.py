def solution():
    """Frank needs to meet a quota at work for his sales. It’s the beginning of the month and in 30 days he needs to have 50 cars sold. The first three days he sold 5 cars each day. Then the next 4 days he sold 3 cars each day. If the month is 30 days long how many cars does he need to sell for the remaining days to meet his quota?"""
    days_left = 30 - 7
    cars_sold = 5*3 + 3*4
    cars_left = 50 - cars_sold
    cars_per_day = cars_left / days_left
    result = cars_per_day
    return result

print(solution())