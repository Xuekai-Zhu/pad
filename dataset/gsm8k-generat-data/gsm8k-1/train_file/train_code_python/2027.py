def solution():
    """Eliza buys 200 ornamental rings to sell in their local shop, twice the number of the remaining stock. After selling 3/4 of the total stock, her mother buys 300 more ornamental rings, and after three days, sells 150. What's the total number of ornamental rings remaining in the store?"""
    initial_stock = 200 / 2
    remaining_stock = initial_stock
    sold_stock = remaining_stock * 3 / 4
    remaining_stock = remaining_stock - sold_stock
    mother_bought = 300
    remaining_stock += mother_bought
    mother_sold = 150
    remaining_stock -= mother_sold
    result = remaining_stock
    return result

print(solution())