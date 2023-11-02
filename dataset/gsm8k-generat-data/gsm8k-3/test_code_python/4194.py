def solution():
    """If a box contains 14 apples, and Henry and his brother each eat 1 apple per day, how many weeks can they spend eating 3 boxes of apples?"""
    # Calculate the total number of apples in 3 boxes
    total_apples = 14 * 3

    # Calculate the daily consumption of apples for both Henry and his brother
    daily_consumption = 2  # 1 apple each

    # Calculate the number of days it will take to eat all the apples
    days_to_finish = total_apples // daily_consumption

    # Convert days to weeks
    weeks_to_finish = days_to_finish / 7

    # Display the number of weeks it will take to eat all the apples
    result = weeks_to_finish
    return result

print(solution())