def solution():
    """Kate saved $27 in March. She saved $13 in April and $28 in May. Then Kate spent $49 on a keyboard and $5 on a mouse. How much money does Kate have left?"""
    march_savings = 27
    april_savings = 13
    may_savings = 28
    total_savings = march_savings + april_savings + may_savings
    keyboard_cost = 49
    mouse_cost = 5
    remaining_money = total_savings - keyboard_cost - mouse_cost
    result = remaining_money
    return result

print(solution())