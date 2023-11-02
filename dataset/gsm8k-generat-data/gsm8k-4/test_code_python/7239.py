def solution():
    """Scout delivers groceries on the weekends. His base pay is $10.00 an hour. He also earns a $5.00 tip per customer that he delivers groceries to. On Saturday he worked 4 hours and delivered groceries to 5 people. Sunday he worked 5 hours and delivered groceries to 8 people. How much did he make over the weekend?"""
    # Define Scout's base pay and pay per delivery
    BASE_PAY = 10
    TIP_PAY = 5

    # Calculate Scout's pay for Saturday
    saturday_pay = (BASE_PAY * 4) + (TIP_PAY * 5)

    # Calculate Scout's pay for Sunday
    sunday_pay = (BASE_PAY * 5) + (TIP_PAY * 8)

    # Calculate Scout's total pay for the weekend
    weekend_pay = saturday_pay + sunday_pay

    result = weekend_pay
    return result

print(solution())