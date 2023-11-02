def solution():
    """Frank needs to meet a quota at work for his sales. It’s the beginning of the month and in 30 days he needs to have 50 cars sold. The first three days he sold 5 cars each day. Then the next 4 days he sold 3 cars each day. If the month is 30 days long how many cars does he need to sell for the remaining days to meet his quota?"""
    # Define the quota and the number of days in the month
    QUOTA = 50
    MONTH_DAYS = 30

    # Calculate the number of cars sold in the first week
    first_week_sales = (5 * 3) + (3 * 4)

    # Calculate the number of days left in the month
    days_left = MONTH_DAYS - 7

    # Calculate the average number of cars Frank needs to sell per day
    cars_per_day = (QUOTA - first_week_sales) / days_left

    # Display the number of cars Frank needs to sell for the remaining days
    result = cars_per_day * (MONTH_DAYS - 7)
    return result

print(solution())