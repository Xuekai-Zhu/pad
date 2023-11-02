def solution():
    """Dorothy earns $60000 a year from her work. She needs to pay 18% of this amount in taxes. How much money will she have left after she pays the taxes?"""
    annual_earnings = 60000
    tax_rate = 0.18
    tax_amount = annual_earnings * tax_rate
    net_earnings = annual_earnings - tax_amount
    result = net_earnings
    return result

print(solution())