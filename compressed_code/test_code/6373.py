def solution():
    
    flour_cost = (500 // 50) * 20
    salt_cost = 10 * 0.2
    total_cost = flour_cost + salt_cost + 1000
    revenue = 20 * 500
    profit = revenue - total_cost
    result = profit
    return result

print(solution())