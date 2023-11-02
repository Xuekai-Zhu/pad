def solution():
    
    cost_adidas = 45
    cost_nike = 60
    cost_reebok = 35
    
    quantity_adidas = 6
    quantity_nike = 8
    quantity_reebok = 9
    
    total_sales = (cost_adidas * quantity_adidas) + (cost_nike * quantity_nike) + (cost_reebok * quantity_reebok)
    
    result = total_sales - 1000
    return result

print(solution())