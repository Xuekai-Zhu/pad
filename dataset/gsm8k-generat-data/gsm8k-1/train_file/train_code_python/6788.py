def solution():
    """It's payday but Jebb has to pay 10% for the tax. If his pay is $650, how much is his take-home pay?"""
    pay = 650
    tax_percent = 10
    tax_amount = pay * (tax_percent / 100)
    take_home_pay = pay - tax_amount
    result = take_home_pay
    return result

print(solution())