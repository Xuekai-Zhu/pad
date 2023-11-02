def solution():
    """To make a living, Carl needs to drive a car for 2 hours every day. After he got promoted he needs to drive for 6 more hours every week. How many hours will Carl drive in two weeks?"""
    # Define the number of hours Carl drives per day
    DAILY_HOURS = 2

    # Define the additional hours Carl drives per week after promotion
    PROMOTION_HOURS = 6

    # Calculate the total number of hours Carl drives in two weeks
    total_hours = (DAILY_HOURS * 14) + (PROMOTION_HOURS * 2)

    # Display the total number of hours
    result = total_hours
    return result

print(solution())