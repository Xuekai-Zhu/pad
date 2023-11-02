def solution():
    # Define the cost of Adidas sneakers
    adidas_cost = 600
    
    # Calculate the cost of Skechers
    skechers_cost = 5 * adidas_cost
    
    # Calculate the cost of Nike sneakers
    nike_cost = 3 * adidas_cost
    
    # Calculate the total cost of sneakers
    total_sneakers_cost = adidas_cost + skechers_cost + nike_cost
    
    # Calculate the cost of clothes
    clothes_cost = 8000 - total_sneakers_cost
    
    result = clothes_cost
    return result

print(solution())