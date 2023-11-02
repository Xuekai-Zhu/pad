def solution():
    """Teresa orders 2 fancy ham and cheese sandwiches for $7.75 each at a local shop. While there, she decides to pick up some salami for $4.00, more brie which is three times the price of the salami, a 1/4 pound of olives that are $10.00 per pound, 1/2 pound of feta cheese that’s $8.00 a pound and another loaf of french bread that is $2.00. How much does she spend at the local shop?"""
    sandwich_price = 7.75
    num_sandwiches = 2
    salami_price = 4.00
    brie_price = 3 * salami_price
    olives_price = 10.00 / 4
    feta_price = 8.00 / 2
    bread_price = 2.00
    total_price = sandwich_price * num_sandwiches + salami_price + brie_price + olives_price + feta_price + bread_price
    result = total_price
    return result

print(solution())