def solution():
    num_reps = 50
    hours_per_day = 8
    pay_per_hour = 14
    num_days = 5

    # Calculate the total number of hours worked by each phone rep
    total_hours = hours_per_day * num_days

    # Calculate the total pay for each phone rep
    total_pay_per_rep = total_hours * pay_per_hour

    # Calculate the total cost to hire all phone reps
    total_cost = total_pay_per_rep * num_reps
    result = total_cost
    return result

print(solution())