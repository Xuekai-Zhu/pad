def solution():
    miles_per_day = 100  # Jon drives 100 miles per day
    days_per_month = 30  # Jon drives for 30 days in a month
    tune_ups_per_1000_miles = 1000  # Jon's car needs a tune-up every 1000 miles

    # Calculate the total number of tune-ups Jon needs in a month
    total_tune_ups = miles_per_day * days_per_month * tune_ups_per_1000_miles
    result = total_tune_ups
    return result

print(solution())