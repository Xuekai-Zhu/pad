def solution():
    daily_jogging_time = 1.5  # Mr. John jogs for 1 hour 30 minutes every day
    days_in_two_weeks = 14  # There are 14 days in two weeks

    # Calculate the total time Mr. John will have spent jogging in two weeks
    total_jogging_time = daily_jogging_time * days_in_two_weeks

    # Convert the total jogging time to hours
    jogging_hours = total_jogging_time / 60
    result = jogging_hours
    return result

print(solution())