def solution():
    current_stock = 164
    initial_stock = 55
    restock = 132

    # Calculate the number of bags of rice that were sold
    sold = initial_stock + restock - current_stock
    result = sold
    return result

print(solution())