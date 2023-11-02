def solution():
    
    pumpkin_pie_cost = 3
    cherry_pie_cost = 5
    total_pumpkin_pie_cost = 10 * pumpkin_pie_cost
    total_cherry_pie_cost = 12 * cherry_pie_cost
    total_cost = total_pumpkin_pie_cost + total_cherry_pie_cost
    total_revenue = total_cost + 20
    total_pies = 10 + 12
    price_per_pie = total_revenue / total_pies
    result = price_per_pie
    return result

print(solution())