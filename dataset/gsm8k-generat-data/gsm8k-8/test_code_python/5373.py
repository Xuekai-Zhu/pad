def solution():
    # Define Jim's gross pay and the percentage going to his retirement account
    gross_pay = 1120
    retirement_percent = 0.25

    # Calculate the amount going to retirement and the amount after taxes
    amount_to_retirement = gross_pay * retirement_percent
    amount_after_taxes = gross_pay - amount_to_retirement - 100

    result = amount_after_taxes
    return result

print(solution())