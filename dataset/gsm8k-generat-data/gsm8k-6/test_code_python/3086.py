def solution():
    # Calculate the total amount paid to all 50 new phone reps after 5 days
    hourly_rate = 14  # hourly pay rate
    work_hours = 8  # daily work hours
    num_reps = 50  # number of new phone reps
    num_days = 5  # number of working days

    total_pay = hourly_rate * work_hours * num_reps * num_days
    result = total_pay
    return result

print(solution())