def solution():
    # Calculate the total cost of the suits
    suit_cost = 2 * 700
    
    # Calculate the total cost of the shirts
    shirt_cost = 6 * 50
    
    # Calculate the total cost of the loafers
    loafer_cost = 2 * 150
    
    # Calculate the total sales
    total_sales = suit_cost + shirt_cost + loafer_cost
    
    # Calculate the commission earned
    commission = 0.15 * total_sales
    result = commission
    return result

print(solution())