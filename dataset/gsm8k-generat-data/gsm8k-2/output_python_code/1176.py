def solution():
    """James rents his car out for $20 an hour. He rents it for 8 hours a day 4 days a week. How much does he make a week?"""
    rent_price = 20
    hours_per_day = 8
    days_per_week = 4
    total_hours = hours_per_day * days_per_week
    total_income = rent_price * total_hours
    result = total_income
    return result

print(solution())