def solution():
    """Linda owns a store. She sells jeans at 11 dollars each and tees at 8 dollars each. If she sold 7 tees and 4 jeans in a day, how much money, in dollars, did she have at the end of the day?"""
    jeans_sold = 4
    tees_sold = 7
    jeans_price = 11
    tees_price = 8
    total_sales = (jeans_sold * jeans_price) + (tees_sold * tees_price)
    result = total_sales
    return result

print(solution())