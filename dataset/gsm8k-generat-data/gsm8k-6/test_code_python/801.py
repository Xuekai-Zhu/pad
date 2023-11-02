def solution():
    # Calculate the amount of money Alex has left after taxes and tithe
    weekly_income = 500
    taxes = 0.1 * weekly_income
    tithe = 0.1 * weekly_income
    water_bill = 55
    left_over = weekly_income - taxes - tithe - water_bill
    result = left_over
    return result

print(solution())