def solution():
    pay_rate_1 = 7
    hours_1 = 3

    pay_rate_2 = 10
    hours_2 = 2

    pay_rate_3 = 12
    hours_3 = 4

    num_days = 5

    # Calculate the total pay from the first job
    pay_1 = pay_rate_1 * hours_1

    # Calculate the total pay from the second job
    pay_2 = pay_rate_2 * hours_2

    # Calculate the total pay from the third job
    pay_3 = pay_rate_3 * hours_3

    # Calculate the total pay for one day
    total_pay = pay_1 + pay_2 + pay_3

    # Calculate the total pay for all five days
    total_pay_week = total_pay * num_days
    result = total_pay_week
    return result

print(solution())