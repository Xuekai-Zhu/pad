def solution():
    """Emily wants to know how much it rained last week. She sees that it rained 2 inches on Monday morning and 1 more inch later that day. It rained twice that much on Tuesday. It did not rain on Wednesday but on Thursday it rained 1 inch. The biggest storm was on Friday when the total was equal to Monday through Thursday combined. What was the daily average rain total for the week?"""
    monday_rain = 2 + 1
    tuesday_rain = monday_rain * 2
    wednesday_rain = 0
    thursday_rain = 1
    friday_rain = monday_rain + tuesday_rain + wednesday_rain + thursday_rain
    total_rain = monday_rain + tuesday_rain + wednesday_rain + thursday_rain + friday_rain
    daily_average = total_rain / 7
    result = daily_average
    return result

print(solution())