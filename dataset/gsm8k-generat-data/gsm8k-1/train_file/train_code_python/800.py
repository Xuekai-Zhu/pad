def solution():
    """Alex gets paid $500 a week and 10% of his weekly income is deducted as tax. He also pays his weekly water bill for $55 and gives away another 10% of his weekly income as a tithe. How much money does Alex have left?"""
    weekly_income = 500
    tax_percent = 10
    tax_amount = weekly_income * (tax_percent / 100)
    take_home_pay = weekly_income - tax_amount - 55
    tithe_percent = 10
    tithe_amount = take_home_pay * (tithe_percent / 100)
    money_left = take_home_pay - tithe_amount
    result = money_left
    return result

print(solution())