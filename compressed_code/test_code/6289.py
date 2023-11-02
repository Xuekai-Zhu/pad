def solution():
    
    price_store1 = 950
    discount1 = 0.06
    price_store2 = 920
    discount2 = 0.05
    final_price1 = price_store1 - (price_store1 * discount1)
    final_price2 = price_store2 - (price_store2 * discount2)
    difference = final_price1 - final_price2
    result = difference
    return result

print(solution())