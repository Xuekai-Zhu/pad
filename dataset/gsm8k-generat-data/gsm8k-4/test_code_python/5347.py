def solution():
    """In a certain country store, there are three kinds of bottled drinks. A cola, which costs $3, a juice for $1.5, and water for $1 per bottle. One day the store was able to sell 15 bottles of cola, 25 bottles of water, and 12 bottles of juice. How much did the shop earn?"""
    # Define the prices and quantities of each drink
    cola_price = 3
    cola_quantity = 15
    juice_price = 1.5
    juice_quantity = 12
    water_price = 1
    water_quantity = 25

    # Calculate the total earnings from selling each drink
    cola_earnings = cola_price * cola_quantity
    juice_earnings = juice_price * juice_quantity
    water_earnings = water_price * water_quantity

    # Calculate the total earnings from selling all the drinks
    total_earnings = cola_earnings + juice_earnings + water_earnings

    # return the result
    result = total_earnings
    return result

print(solution())