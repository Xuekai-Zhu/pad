def solution():
    """Marco uses a fifth of an ounce of dry tea leaves to brew his morning cup of tea each day. He buys tea leaves in boxes of 28 ounces. How many weeks of daily tea does Marco get from a box?"""
    # Define the amount of tea leaves used per day and per week
    daily_tea_leaves = 1/5
    weekly_tea_leaves = daily_tea_leaves * 7

    # Define the size of the tea leaves box
    box_size = 28

    # Calculate the number of weeks of daily tea from a box
    weeks_of_tea = box_size / weekly_tea_leaves

    # Return the result rounded to two decimal places
    result = round(weeks_of_tea, 2)
    return result

print(solution())