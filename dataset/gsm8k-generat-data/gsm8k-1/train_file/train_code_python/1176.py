def solution():
    """James rents his car out for $20 an hour. He rents it for 8 hours a day 4 days a week. How much does he make a week?"""
    rental_rate = 20
    hours_rented_per_day = 8
    days_rented_per_week = 4
    total_hours_rented = hours_rented_per_day * days_rented_per_week
    total_money_made = rental_rate * total_hours_rented
    result = total_money_made
    return result

print(solution())