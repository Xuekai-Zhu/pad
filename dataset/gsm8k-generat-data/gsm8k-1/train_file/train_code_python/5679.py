def solution():
    """Ten percent of Jonessa's pay goes to paying tax. If her pay is $500, how much is her take-home pay?"""
    total_pay = 500
    tax_percent = 10
    tax_amount = total_pay * (tax_percent / 100)
    take_home_pay = total_pay - tax_amount
    result = take_home_pay
    return result

print(solution())