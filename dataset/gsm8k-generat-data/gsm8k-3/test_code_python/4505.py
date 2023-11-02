def solution():
    """Unrest leads to 30 days of protest in 21 different cities.  In each city, there are 10 arrests per day.  The average person spends 4 days in jail before trial and then spends half of a 2-week sentence.  How many combined weeks of jail time are there?"""
    # Define the number of days of protest and number of cities
    protest_days = 30
    cities = 21

    # Define the number of arrests per day in each city
    arrests_per_day = 10

    # Calculate the total number of arrests
    total_arrests = protest_days * cities * arrests_per_day

    # Calculate the total number of days spent in jail before trial
    days_before_trial = total_arrests * 4

    # Calculate the total number of weeks spent in jail after trial
    weeks_after_trial = (total_arrests * 14) / 2 / 7

    # Calculate the total combined weeks of jail time
    total_weeks = days_before_trial / 7 + weeks_after_trial

    # Display the total combined weeks of jail time
    result = total_weeks
    return result

print(solution())