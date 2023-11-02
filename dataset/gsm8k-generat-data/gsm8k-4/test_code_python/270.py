def solution():
    """Ayla has a customer care job whose primary role is to hear complaints from customers and advise them on the best way to solve their problems. She talks with each customer for a limited amount of time, and each phone call is charged five cents per minute. If each call lasts 1 hour, what's the phone bill at the end of the month if she manages to talk to 50 customers a week?"""
    # Define the variables
    minutes_per_week = 60 * 60
    total_minutes = minutes_per_week * 4  # 4 weeks in a month
    cost_per_minute = 0.05
    num_customers = 50
    call_duration = 60  # 1 hour

    # Calculate the total cost of phone calls
    total_cost = num_customers * total_minutes * call_duration * cost_per_minute

    # return the result
    result = total_cost
    return result

print(solution())