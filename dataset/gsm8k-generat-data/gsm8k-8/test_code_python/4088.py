def solution():
    # Calculate the total pay for the first 40 hours
    pay_40_hours = 20 * 40

    # Calculate the pay for the remaining 10 hours (double the regular rate)
    pay_extra_hours = 2 * 20 * 10

    # Calculate the total pay for the 50-hour workweek
    total_pay = pay_40_hours + pay_extra_hours
    result = total_pay
    return result

print(solution())