def solution():
    """Tim decides to start selling necklaces he makes. He uses 10 charms to make each necklace. Each charm cost $15. He sells the necklace for $200. How much profit does he make if he sells 30?"""
    charms_per_necklace = 10
    charm_cost = 15
    selling_price = 200
    necklaces_sold = 30
    
    total_material_cost = charms_per_necklace * charm_cost * necklaces_sold
    total_sales = selling_price * necklaces_sold
    profit = total_sales - total_material_cost
    
    result = profit
    return result

print(solution())