def solution():
    gross_pay = 650  # Jebb's gross pay is $650
    tax_rate = 0.1  # Jebb has to pay 10% for taxes

    # Calculate the amount of tax Jebb has to pay
    tax_amount = gross_pay * tax_rate

    # Calculate Jebb's take-home pay
    take_home_pay = gross_pay - tax_amount
    result = take_home_pay
    return result

print(solution())