def solution():
    """A salesman bought a case of 48 sneakers for $576. He sold 17 of them for $20 at a flash sale on Monday, and the rest were sold to a department store for $25 each throughout the rest of the week. How much money, in dollars, was the salesman's profit?"""
    total_cost = 576
    sneakers_per_case = 48
    flash_sale_price = 20
    department_store_price = 25
    flash_sale_sneakers = 17
    department_store_sneakers = sneakers_per_case - flash_sale_sneakers
    flash_sale_revenue = flash_sale_sneakers * flash_sale_price
    department_store_revenue = department_store_sneakers * department_store_price
    total_revenue = flash_sale_revenue + department_store_revenue
    profit = total_revenue - total_cost
    result = profit
    
    return result

print(solution())