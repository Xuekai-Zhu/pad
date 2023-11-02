def solution():
    """To make a living, Carl needs to drive a car for 2 hours every day. After he got promoted he needs to drive for 6 more hours every week. How many hours will Carl drive in two weeks?"""
    # Define the number of hours Carl drives per day
    daily_hours = 2

    # Define the number of additional hours Carl drives per week after promotion
    weekly_hours = 6

    # Calculate the total hours Carl drives in one week
    weekly_total = daily_hours * 7 + weekly_hours

    # Calculate the total hours Carl drives in two weeks
    total_hours = weekly_total * 2

    result = total_hours
    return result

print(solution())