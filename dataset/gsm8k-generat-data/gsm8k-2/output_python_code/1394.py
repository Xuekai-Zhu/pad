def solution():
    """Mike bought a DVD of his favorite movie. He paid $5 for it at the store. A friend of Mike's, Steve, saw this and also decided to buy a DVD of the movie, but it was already sold out. He needed to order it online, which cost him twice as much. And in addition, he needed to pay the shipping costs which were 80% of the price of the film he ordered. How much did Steve pay to get the DVD in total?"""
    mike_price = 5
    steve_price = 2 * mike_price
    shipping_price = 0.8 * steve_price
    total_price = steve_price + shipping_price
    result = total_price
    return result

print(solution())