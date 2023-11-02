def solution():
    """Flynn watches 30 minutes of tv every night during the weekdays. On the weekends, she watches an additional 2 hours of TV in total. How many hours of tv does she watch in 52 weeks?"""
    
    # Calculate the total minutes of TV watched during the weekdays in a week
    weekdays_minutes = 30 * 5 # 30 minutes every night for 5 days

    # Calculate the total hours watched during the weekends in a week
    weekends_hours = 2 # 2 additional hours on the weekends

    # Calculate the total hours watched in a week
    total_hours = (weekdays_minutes + weekends_hours*60) / 60

    # Calculate the total hours of TV watched in 52 weeks
    total_hours_52_weeks = total_hours * 52

    # Return the result rounded to 2 decimal places
    result = round(total_hours_52_weeks, 2)
    return result

print(solution())