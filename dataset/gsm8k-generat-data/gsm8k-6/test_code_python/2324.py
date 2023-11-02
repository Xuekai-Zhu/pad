def solution():
    hourly_rate = 5  # Isabella earns $5 an hour babysitting
    hours_per_day = 5  # Isabella babysits 5 hours every day
    afternoons_per_week = 6  # Isabella babysits 6 afternoons a week
    weeks = 7  # Isabella babysits for 7 weeks

    # Calculate the total amount of money earned by Isabella
    total_earnings = hourly_rate * hours_per_day * afternoons_per_week * weeks
    result = total_earnings
    return result

print(solution())