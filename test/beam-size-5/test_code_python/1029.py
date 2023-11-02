def solution():
    hours_per_day = 6
    num_days = 3
    court_case_pay = 15
    parking_pay = 3

    # Calculate the total pay for the court case
    court_case_pay = hours_per_day * court_case_pay

    # Calculate the total pay for parking
    parking_pay = parking_pay * num_days

    # Calculate the total pay for all expenses
    total_expenses = court_case_pay + parking_pay

    # Calculate the pay per hour after expenses
    pay_per_hour_after_expenses = total_expenses / hours_per_day
    result = pay_per_hour_after_expenses
    return result

print(solution())