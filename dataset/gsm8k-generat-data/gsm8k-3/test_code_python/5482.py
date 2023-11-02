def solution():
    """Rachel drinks 2 glasses of water on Sunday and 4 glasses of water on Monday. Then she drinks 3 glasses of water every day for the next 4 days. One glass of water is 10 ounces of water. If Rachel wants to drink a total of 220 ounces of water in the week (Sunday to Saturday), how many glasses of water should she drink on Saturday?"""
    # Define the number of glasses of water Rachel drinks each day
    SUNDAY_GLASSES = 2
    MONDAY_GLASSES = 4
    WEEKDAY_GLASSES = 3

    # Calculate the total number of ounces Rachel drinks on Sunday and Monday
    sunday_ounces = SUNDAY_GLASSES * 10
    monday_ounces = MONDAY_GLASSES * 10

    # Calculate the total number of ounces Rachel drinks on the weekdays
    weekday_ounces = WEEKDAY_GLASSES * 10 * 4

    # Calculate the remaining number of ounces Rachel needs to drink on Saturday
    remaining_ounces = 220 - sunday_ounces - monday_ounces - weekday_ounces

    # Calculate the number of glasses of water Rachel should drink on Saturday
    saturday_glasses = remaining_ounces / 10

    # Display the number of glasses of water Rachel should drink on Saturday
    result = saturday_glasses
    return result

print(solution())