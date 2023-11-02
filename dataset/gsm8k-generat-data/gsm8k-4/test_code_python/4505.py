def solution():
    """Unrest leads to 30 days of protest in 21 different cities. In each city, there are 10 arrests per day. 
    The average person spends 4 days in jail before trial and then spends half of a 2-week sentence.
    How many combined weeks of jail time are there?"""
    
    # Define the number of days of protest, the number of cities, and the number of arrests per day in each city
    days_of_protest = 30
    num_cities = 21
    arrests_per_day = 10

    # Calculate the total number of arrests during the protest
    total_arrests = days_of_protest * num_cities * arrests_per_day

    # Calculate the total number of days spent in jail before trial
    pre_trial_days = total_arrests * 4

    # Calculate the total number of days spent in jail after trial
    post_trial_days = total_arrests * 7

    # Calculate the total number of weeks spent in jail
    total_weeks = (pre_trial_days + post_trial_days) / (7*2)

    # Return the result
    return round(total_weeks)

print(solution())