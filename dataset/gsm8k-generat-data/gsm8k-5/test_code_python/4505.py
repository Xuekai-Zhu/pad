def solution():
    days_of_protest = 30  # There are 30 days of protest
    cities = 21  # Protests take place in 21 different cities
    arrests_per_day = 10  # There are 10 arrests per day in each city

    # Calculate the total number of arrests during the protests
    total_arrests = days_of_protest * cities * arrests_per_day

    # Calculate the total number of days spent in jail before trial
    pretrial_days = total_arrests * 4

    # Calculate the total number of weeks spent in jail after sentencing
    sentence_weeks = total_arrests * 0.5

    # Calculate the combined total of pretrial and sentence weeks
    total_weeks = (pretrial_days / 7) + sentence_weeks
    result = total_weeks
    return result

print(solution())