def solution():
    
    cost_price = 20
    profit_percentage = 30
    selling_price = cost_price + ((profit_percentage/100) * cost_price)
    sale_percentage = 50
    final_price = selling_price - ((sale_percentage/100) * selling_price)
    result = final_price
    return result

print(solution())