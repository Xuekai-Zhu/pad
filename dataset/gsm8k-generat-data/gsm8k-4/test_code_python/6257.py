def solution():
    """Droid owns a coffee shop. He uses 3 bags of coffee beans every morning, he uses triple that number in the afternoon than in the morning, and he uses twice the morning number in the evening. How many bags of coffee beans does he use every week?"""
    # Define the number of bags of coffee beans used in the morning
    morning_coffee = 3

    # Define the number of bags of coffee beans used in the afternoon, which is triple the morning amount
    afternoon_coffee = morning_coffee * 3

    # Define the number of bags of coffee beans used in the evening, which is twice the morning amount
    evening_coffee = morning_coffee * 2

    # Define the total number of bags of coffee beans used in a day
    daily_coffee = morning_coffee + afternoon_coffee + evening_coffee

    # Define the total number of bags of coffee beans used in a week
    weekly_coffee = daily_coffee * 7

    # return the result
    result = weekly_coffee
    return result

print(solution())