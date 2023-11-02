def solution():
    """Frank needs to meet a quota at work for his sales. It’s the beginning of the month and in 30 days he needs to have 50 cars sold. The first three days he sold 5 cars each day. Then the next 4 days he sold 3 cars each day. If the month is 30 days long how many cars does he need to sell for the remaining days to meet his quota?"""
    total_days = 30
    quota = 50
    sold_first_3_days = 5 * 3
    sold_next_4_days = 3 * 4
    total_sold = sold_first_3_days + sold_next_4_days
    remaining_days = total_days - 7
    remaining_quota = quota - total_sold
    remaining_cars_per_day = remaining_quota / remaining_days
    result = remaining_cars_per_day
    return result

print(solution())