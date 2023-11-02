def solution():
    
    initial_cost = 300
    final_sale_price = 255
    percentage_lost = ((initial_cost - final_sale_price) / initial_cost) * 100
    result = percentage_lost
    return result

print(solution())