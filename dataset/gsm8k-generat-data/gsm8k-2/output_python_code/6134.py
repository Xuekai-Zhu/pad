def solution():
    """A trader has 55 bags of rice in stock. She sells off some bags of rice and restocks 132 bags of rice. How many bags of rice did she sell if she now has 164 bags of rice?"""
    initial_stock = 55
    restock = 132
    final_stock = 164
    sold = initial_stock + restock - final_stock
    result = sold
    return result

print(solution())