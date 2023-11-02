def solution():
    # Calculate the total cost of making 25 bracelets
    total_cost = (1+3)*25  # $1 for string and $3 for beads per bracelet, multiplied by 25 bracelets
    
    # Calculate the total revenue from selling 25 bracelets
    total_revenue = 6*25  # $6 per bracelet, multiplied by 25 bracelets
    
    # Calculate the profit from selling 25 bracelets
    profit = total_revenue - total_cost
    
    result = profit
    return result

print(solution())