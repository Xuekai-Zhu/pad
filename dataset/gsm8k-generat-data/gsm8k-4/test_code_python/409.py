def solution():
    """Frank needs to meet a quota at work for his sales. It’s the beginning of the month and in 30 days he needs to have 50 cars sold. The first three days he sold 5 cars each day. Then the next 4 days he sold 3 cars each day. If the month is 30 days long how many cars does he need to sell for the remaining days to meet his quota?"""
    # Define the quota and the number of days left in the month
    quota = 50
    days_left = 30 - 3 - 4

    # Calculate the number of cars sold in the first week
    cars_sold_first_week = 5 * 3 + 3 * 4

    # Calculate the remaining quota to be met
    remaining_quota = quota - cars_sold_first_week

    # Calculate the daily quota for the remaining days
    daily_quota = remaining_quota / days_left

    # Round up to the nearest integer to account for fractional cars
    remaining_cars_to_sell = int(round(daily_quota))

    # return the result
    result = remaining_cars_to_sell
    return result

print(solution())