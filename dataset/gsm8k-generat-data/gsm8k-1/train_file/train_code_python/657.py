def solution():
    """Sara is checking out two different stores to buy a computer. The first store offers a device for $950 with a 6% discount. The second sells the same computer for €920 with a 5% discount. What is the difference in price between the two stores?"""
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