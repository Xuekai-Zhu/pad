def solution():
    ajax_weight_in_pounds = 80 * 2.2  # Ajax weighs 80 kilograms, which is equal to 176 pounds
    pounds_lost_per_hour = 1.5  # Exercising for an hour helps Ajax lose 1.5 pounds
    hours_per_day = 2  # Ajax plans to exercise for 2 hours every day
    days_per_week = 7  # There are 7 days in a week
    weeks = 2  # Ajax plans to exercise for 2 weeks

    # Calculate the total number of pounds Ajax will lose in 2 weeks
    total_pounds_lost = pounds_lost_per_hour * hours_per_day * days_per_week * weeks

    # Calculate Ajax's weight in pounds after 2 weeks
    ajax_weight_in_pounds -= total_pounds_lost
    result = ajax_weight_in_pounds
    return result

print(solution())