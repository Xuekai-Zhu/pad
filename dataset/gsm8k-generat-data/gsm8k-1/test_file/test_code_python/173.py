def solution():
    """Zaid spends 1/4 of his salary on rent, 1/3 on car fuel and donates half of the remaining amount to his favorite charity. 
    He gives his daughter 200$ to use for her weekly expenses and 700$ to his wife to budget for groceries and other household goods. 
    If Zaid earns 6000$ per month, how much money will he still have after all these expenses and donations?"""
    salary = 6000
    rent = salary * 1/4
    fuel = salary * 1/3
    remaining = salary - rent - fuel
    charity = remaining * 1/2
    remaining = remaining - charity - 200 - 700
    result = remaining
    return result

print(solution())