def solution():
    """Ayla has a customer care job whose primary role is to hear complaints from customers and advise them on the best way to solve their problems. She talks with each customer for a limited amount of time, and each phone call is charged five cents per minute. If each call lasts 1 hour, what's the phone bill at the end of the month if she manages to talk to 50 customers a week?"""
    minutes_per_call = 60
    calls_per_week = 50
    weekly_cost = minutes_per_call * 5 * calls_per_week
    monthly_cost = weekly_cost * 4
    result = monthly_cost
    return result

print(solution())