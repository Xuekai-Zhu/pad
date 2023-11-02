def solution():
    """Fern buys one pair of high heels for $60 and five pairs of ballet slippers for 2/3rds of the price of the high heels. How much does she pay total?"""
    high_heels_price = 60
    ballet_slippers_price = (2/3) * high_heels_price
    total_price = high_heels_price + (5 * ballet_slippers_price)
    result = total_price
    return result

print(solution())