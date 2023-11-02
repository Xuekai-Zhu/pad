def solution():
    num_employees = 100
    junior_programmers = (2/5) * num_employees
    senior_programmers = junior_programmers + 400
    monthly_payment = 2000

    # Calculate the total amount paid to all programmers per month
    total_payment = (num_employees * monthly_payment) + (num_junior_programmers * monthly_payment)
    result = total_payment
    return result

print(solution())