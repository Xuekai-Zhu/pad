def solution():
    """Robby, Jaylen and Miranda are employed at a Cheesecake factory, earning $10 per hour. They work 10 hours a day, five days a week. Robby saves 2/5 of his salary, Jaylene saves 3/5 of his salary, while Miranda saves half of her salary. What are the combined savings of the three employees after four weeks?"""
    hourly_rate = 10
    hours_per_day = 10
    days_per_week = 5
    weeks = 4

    # calculating weekly earnings for each employee
    robby_earnings = hourly_rate * hours_per_day * days_per_week
    jaylen_earnings = hourly_rate * hours_per_day * days_per_week
    miranda_earnings = hourly_rate * hours_per_day * days_per_week

    # calculating weekly savings for each employee
    robby_savings = robby_earnings * (2/5)
    jaylen_savings = jaylen_earnings * (3/5)
    miranda_savings = miranda_earnings * 0.5

    # calculating total savings for all three employees after four weeks
    total_savings = (robby_savings + jaylen_savings + miranda_savings) * weeks

    result = total_savings
    return result

print(solution())