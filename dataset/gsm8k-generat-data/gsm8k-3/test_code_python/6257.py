def solution():
    """Droid owns a coffee shop. He uses 3 bags of coffee beans every morning, he uses triple that number in the afternoon than in the morning, and he uses twice the morning number in the evening. How many bags of coffee beans does he use every week?"""
    # Define the coffee beans used in the morning
    morning_beans = 3

    # Define the coffee beans used in the afternoon
    afternoon_beans = morning_beans * 3

    # Define the coffee beans used in the evening
    evening_beans = morning_beans * 2

    # Calculate the total coffee beans used in a day
    daily_beans = morning_beans + afternoon_beans + evening_beans

    # Calculate the total coffee beans used in a week
    weekly_beans = daily_beans * 7

    # Display the total coffee beans used in a week
    result = weekly_beans
    return result

print(solution())