def solution():
    """It's payday but Jebb has to pay 10% for the tax. If his pay is $650, how much is his take-home pay?"""
    pay = 650
    tax = 0.1 * pay
    take_home_pay = pay - tax
    result = take_home_pay
    return result

print(solution())