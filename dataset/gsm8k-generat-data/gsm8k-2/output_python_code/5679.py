def solution():
    """Ten percent of Jonessa's pay goes to paying tax. If her pay is $500, how much is her take-home pay?"""
    pay = 500
    tax_percent = 10
    tax_amount = (tax_percent / 100) * pay
    take_home_pay = pay - tax_amount
    result = take_home_pay
    return result

print(solution())