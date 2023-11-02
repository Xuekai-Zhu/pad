def solution():
    hourly_rate = 10  # Jamie earns $10 an hour
    delivery_days_per_week = 2  # Jamie delivers flyers 2 days each week
    hours_per_delivery = 3  # Jamie spends 3 hours each time she delivers flyers
    weeks = 6  # Jamie delivers flyers for 6 weeks

    # Calculate the total number of hours Jamie works
    total_hours = delivery_days_per_week * hours_per_delivery * weeks

    # Calculate the total amount of money Jamie earns
    total_earnings = hourly_rate * total_hours
    result = total_earnings
    return result

print(solution())