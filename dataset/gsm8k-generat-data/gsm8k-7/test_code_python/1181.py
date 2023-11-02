def solution():
    hours_worked = [10, 8, 15]
    pay_rate = 10

    # Calculate the total number of hours worked by both men
    total_hours_worked = sum(hours_worked)

    # Calculate the total amount of money earned by each man
    total_pay_per_man = total_hours_worked * pay_rate

    # Calculate the total amount paid to both men
    total_pay = total_pay_per_man * 2
    result = total_pay
    return result

print(solution())