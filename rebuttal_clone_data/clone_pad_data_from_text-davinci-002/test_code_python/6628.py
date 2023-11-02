def solution():
    
    customers = 20
    customers_buying_2 = 4
    customers_buying_1 = 12
    customers_buying_4 = 4
    
    total_paintings_sold = (customers_buying_2 * 2) + (customers_buying_1 * 1) + (customers_buying_4 * 4)
    
    result = total_paintings_sold
    
    return result

print(solution())