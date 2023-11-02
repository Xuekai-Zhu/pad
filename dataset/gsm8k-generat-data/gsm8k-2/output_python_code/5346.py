def solution():
    """In a certain country store, there are three kinds of bottled drinks. A cola, which costs $3, a juice for $1.5, and water for $1 per bottle. One day the store was able to sell 15 bottles of cola, 25 bottles of water, and 12 bottles of juice. How much did the shop earn?"""
    cola_price = 3
    juice_price = 1.5
    water_price = 1
    cola_sales = 15
    juice_sales = 12
    water_sales = 25
    total_sales = (cola_price * cola_sales) + (juice_price * juice_sales) + (water_price * water_sales)
    result = total_sales
    return result

print(solution())