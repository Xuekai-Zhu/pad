def solution():
    tax_rate = 0.1  # 10%
    pay = 500

    # Calculate the amount of tax to be paid
    tax = pay * tax_rate

    # Calculate Jonessa's take-home pay
    take_home_pay = pay - tax
    result = take_home_pay
    return result

print(solution())