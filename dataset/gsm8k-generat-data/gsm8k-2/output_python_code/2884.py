def solution():
    """Tina saved $27 in June, $14 in July, and $21 in August. Then Tina spent $5 on books and $17 on new shoes. How much money does Tina have left?"""
    june_savings = 27
    july_savings = 14
    august_savings = 21
    books_cost = 5
    shoes_cost = 17
    total_savings = june_savings + july_savings + august_savings
    total_spending = books_cost + shoes_cost
    remaining_money = total_savings - total_spending
    result = remaining_money
    return result

print(solution())