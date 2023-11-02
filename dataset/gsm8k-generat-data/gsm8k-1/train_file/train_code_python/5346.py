def solution():
    """In a certain country store, there are three kinds of bottled drinks. A cola, which costs $3, a juice for $1.5, and water for $1 per bottle. One day the store was able to sell 15 bottles of cola, 25 bottles of water, and 12 bottles of juice. How much did the shop earn?"""
    cola_price = 3
    juice_price = 1.5
    water_price = 1
    cola_sold = 15
    juice_sold = 12
    water_sold = 25
    total_sales = (cola_price*cola_sold) + (juice_price*juice_sold) + (water_price*water_sold)
    result = total_sales
    return result

print(solution())