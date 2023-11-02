def solution():
    # Define the number of phone reps, hours worked per day, and hourly wage
    num_reps = 50
    hours_per_day = 8
    wage_per_hour = 14.00

    # Calculate the total pay for each phone rep for 5 days of work
    total_pay_per_rep = hours_per_day * wage_per_hour * 5

    # Calculate the total pay for all 50 phone reps for 5 days of work
    total_pay_all_reps = num_reps * total_pay_per_rep
    result = total_pay_all_reps
    return result

print(solution())