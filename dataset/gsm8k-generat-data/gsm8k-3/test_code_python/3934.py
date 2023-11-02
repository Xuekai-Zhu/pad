def solution():
    """Janet goes to the gym for 5 hours a week.  She goes Monday, Tuesday,
    Wednesday, and Friday.  She spends an hour and a half each day on Monday
    and Wednesday.  If she spends the same amount of time at the gym on Tuesday
    and Friday how many hours is she at the gym on Friday?"""
    # Define the amount of time Janet spends at the gym on Monday and
    # Wednesday
    monday_wednesday_time = 1.5

    # Define the total amount of time Janet spends at the gym
    total_time = 5

    # Calculate the amount of time Janet spends at the gym on Tuesday and
    # Friday
    tuesday_friday_time = (total_time - 2 * monday_wednesday_time) / 2

    # Display the amount of time Janet spends at the gym on Friday
    result = tuesday_friday_time
    return result

print(solution())