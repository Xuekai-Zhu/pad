def solution():
    weekly_charge = 300
    total_amount = 1800
    payment_interval = 2

    # Calculate the total number of payments Grace will receive
    num_payments = total_amount / (weekly_charge * payment_interval)

    # Calculate the total number of weeks it will take for Grace to get the desired amount
    num_weeks = num_payments * payment_interval
    result = num_weeks
    return result

print(solution())