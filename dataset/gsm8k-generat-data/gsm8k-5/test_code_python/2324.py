def solution():
    hourly_rate = 5  # Isabella earns $5 an hour babysitting
    hours_per_day = 5  # Isabella babysits 5 hours every day
    afternoons_per_week = 6  # Isabella babysits 6 afternoons a week
    weeks = 7  # Isabella has babysat for 7 weeks

    # Calculate her total hours babysitting
    total_hours = hours_per_day * afternoons_per_week * weeks

    # Calculate her total earnings
    total_earnings = total_hours * hourly_rate

    result = total_earnings
    return result

print(solution())