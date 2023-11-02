def solution():
    long_sleeve_cost = 15
    striped_cost = 10
    total_cost = 80
    
    # Calculating the cost of the four long-sleeved jerseys
    long_sleeve_total = 4 * long_sleeve_cost
    
    # Calculating the cost of the striped jerseys
    striped_total = total_cost - long_sleeve_total
    
    # Calculating the number of striped jerseys Justin bought
    striped_qty = striped_total / striped_cost
    result = striped_qty
    return result

print(solution())