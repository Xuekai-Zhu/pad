def solution():
    burger_cost = 6.0
    soda_cost = burger_cost / 3
    num_burgers = 1
    num_sodas = 1
    
    # Calculate the total cost of Paulo's order
    paulo_total = (num_burgers * burger_cost) + (num_sodas * soda_cost)
    
    # Calculate the total cost of Jeremy's order
    jeremy_total = (num_burgers * 2 * burger_cost) + (num_sodas * 2 * soda_cost)
    
    # Calculate the combined total cost of both their orders
    combined_total = paulo_total + jeremy_total
    result = combined_total
    return result

print(solution())