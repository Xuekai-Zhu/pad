def solution():
    """Dorothy earns $60000 a year from her work. She needs to pay 18% of this amount in taxes. How much money will she have left after she pays the taxes?"""
    income = 60000
    tax_percent = 18
    tax_amount = income * (tax_percent / 100)
    take_home_pay = income - tax_amount
    result = take_home_pay
    return result

print(solution())