def solution():
    hours_per_day = 12
    days_per_month = 30
    original_rate = 20
    raise_percentage = 30/100

    # Calculate the new hourly rate with the raise
    new_rate = original_rate + (original_rate * raise_percentage)

    # Calculate the total hours John works in a month
    total_hours = (days_per_month // 2) * hours_per_day

    # Calculate John's total earnings in a month
    total_earnings = new_rate * total_hours
    result = total_earnings
    return result

print(solution())