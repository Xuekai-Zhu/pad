def solution():
    """Ayla has a customer care job whose primary role is to hear complaints from customers and advise them
    on the best way to solve their problems. She talks with each customer for a limited amount of time, and 
    each phone call is charged five cents per minute. If each call lasts 1 hour, what's the phone bill at the
    end of the month if she manages to talk to 50 customers a week?"""
    minutes_per_call = 60 
    cost_per_min = 0.05
    calls_per_week = 50
    total_minutes_per_week = calls_per_week * minutes_per_call
    cost_per_week = total_minutes_per_week * cost_per_min
    total_cost_in_a_month = cost_per_week * 4
    result = total_cost_in_a_month
    return result

print(solution())