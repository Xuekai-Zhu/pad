def solution():
    """Kate saved $27 in March. She saved $13 in April and $28 in May. Then Kate spent $49 on a keyboard and $5 on a mouse. How much money does Kate have left?"""
    total_savings = 27 + 13 + 28
    total_spending = 49 + 5
    remaining_money = total_savings - total_spending
    result = remaining_money
    return result

print(solution())