def solution():
    """Emily wants to know how much it rained last week. She sees that it rained 2 inches on Monday morning and 1 more inch later that day. It rained twice that much on Tuesday. It did not rain on Wednesday but on Thursday it rained 1 inch. The biggest storm was on Friday when the total was equal to Monday through Thursday combined. What was the daily average rain total for the week?"""
    # Define the amount of rain each day
    monday_morning = 2
    monday_afternoon = 1
    tuesday = monday_morning * 2
    wednesday = 0
    thursday = 1
    friday = monday_morning + monday_afternoon + tuesday + thursday

    # Calculate the total amount of rain for the week
    total_rain = monday_morning + monday_afternoon + tuesday + wednesday + thursday + friday

    # Calculate the daily average rain total for the week
    daily_average = total_rain / 7

    # Display the daily average rain total for the week
    result = daily_average
    return result

print(solution())