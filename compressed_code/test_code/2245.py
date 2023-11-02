def solution():
    
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