def solution():
    """Jon's car needs a tune-up every 1000 miles. He drives 100 miles a day for a 30 day month. How many tune-ups does he need in that time?"""
    miles_per_day = 100
    days_in_month = 30
    miles_in_month = miles_per_day * days_in_month
    tune_ups_needed = miles_in_month / 1000
    result = tune_ups_needed
    return result

print(solution())