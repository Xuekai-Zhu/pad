def solution():
    hourly_rate = 60
    hours_per_day = 3
    num_days = 14

    # Calculate the total number of hours worked by the magician
    total_hours = hours_per_day * num_days

    # Calculate the total payment to the magician
    total_payment = total_hours * hourly_rate
    result = total_payment
    return result

print(solution())