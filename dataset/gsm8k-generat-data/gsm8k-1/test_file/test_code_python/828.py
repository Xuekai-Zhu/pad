def solution():
    """Roy has saved 40% more in money earned by chores than his brother Anthony. Anthony has saved $10.00 more than their sister Eva. Eva has saved $20.00. How much money does Roy have?"""
    eva_savings = 20
    anthony_savings = eva_savings + 10
    roy_savings = anthony_savings * 1.4
    result = roy_savings
    return result

print(solution())