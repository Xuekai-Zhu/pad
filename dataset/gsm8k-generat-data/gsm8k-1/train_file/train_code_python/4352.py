def solution():
    """Norris saved $29 in September. He saved $25 in October and $31 in November. Then Hugo spent $75 on an online game. How much money does Norris have left?"""
    september_savings = 29
    october_savings = 25
    november_savings = 31
    total_savings = september_savings + october_savings + november_savings
    money_left = total_savings - 75
    result = money_left
    return result

print(solution())