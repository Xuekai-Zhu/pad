def solution():
    """Eliza buys 200 ornamental rings to sell in their local shop, twice the number of the remaining stock. After selling 3/4 of the total stock, her mother buys 300 more ornamental rings, and after three days, sells 150. What's the total number of ornamental rings remaining in the store?"""
    
    # Define the initial number of rings and the number Eliza bought
    initial_rings = 0
    bought_rings = 200
    
    # Calculate the initial number of rings based on Eliza buying twice the remaining stock
    remaining_stock = (bought_rings / 2)
    initial_rings = remaining_stock + bought_rings
    
    # Calculate the number of rings sold after Eliza sold 3/4 of the total stock
    sold_rings = (3/4) * initial_rings
    
    # Update the remaining stock after Eliza's mother bought 300 more rings
    remaining_stock = initial_rings + 300
    
    # Update the remaining stock after selling 150 rings
    remaining_stock = remaining_stock - 150
    
    # Return the final number of rings remaining in the store
    result = remaining_stock
    return result

print(solution())