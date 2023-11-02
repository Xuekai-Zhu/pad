def solution():
    """Ayla has a customer care job whose primary role is to hear complaints from customers and advise them on the best way to solve their problems. She talks with each customer for a limited amount of time, and each phone call is charged five cents per minute. If each call lasts 1 hour, what's the phone bill at the end of the month if she manages to talk to 50 customers a week?"""
    # Define the cost per minute
    COST_PER_MINUTE = 0.05

    # Calculate the number of minutes per call
    minutes_per_call = 60

    # Define the number of customers Ayla talks to per week
    customers_per_week = 50

    # Calculate the total number of minutes Ayla spends on the phone per week
    minutes_per_week = customers_per_week * minutes_per_call

    # Calculate the total cost for one week
    cost_per_week = minutes_per_week * COST_PER_MINUTE

    # Calculate the total cost for one month (assuming 4 weeks in a month)
    cost_per_month = cost_per_week * 4

    # Display the total cost for the month
    result = cost_per_month
    return result

print(solution())