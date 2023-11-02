def solution():
    pay = 650
    tax_percent = 0.1  # 10% tax rate

    # Calculate the amount of tax Jebb has to pay
    tax = pay * tax_percent

    # Calculate Jebb's take-home pay
    take_home_pay = pay - tax
    result = take_home_pay
    return result

print(solution())