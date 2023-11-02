def solution():
    """It's payday but Jebb has to pay 10% for the tax. If his pay is $650, how much is his take-home pay?"""
    # Define Jebb's pay and tax rate
    pay = 650
    tax_rate = 0.1

    # Calculate the amount of tax and take-home pay
    tax = pay * tax_rate
    take_home_pay = pay - tax

    # Return the result
    result = take_home_pay
    return result

print(solution())