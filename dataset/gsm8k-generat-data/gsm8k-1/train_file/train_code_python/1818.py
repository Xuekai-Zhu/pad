def solution():
    """Teresa orders 2 fancy ham and cheese sandwiches for $7.75 each at a local shop. While there, she decides to pick up some salami for $4.00, more brie which is three times the price of the salami, a 1/4 pound of olives that are $10.00 per pound, 1/2 pound of feta cheese that’s $8.00 a pound and another loaf of french bread that is $2.00. How much does she spend at the local shop?"""
    sandwich_price = 7.75
    num_sandwiches = 2
    salami_price = 4.00
    brie_price = 3 * salami_price
    olives_price_per_pound = 10.00
    olives_amount = 0.25
    feta_price_per_pound = 8.00
    feta_amount = 0.5
    bread_price = 2.00
    
    sandwich_total = sandwich_price * num_sandwiches
    salami_total = salami_price
    brie_total = brie_price
    olives_total = olives_amount * olives_price_per_pound
    feta_total = feta_amount * feta_price_per_pound
    bread_total = bread_price
    
    total_spent = sandwich_total + salami_total + brie_total + olives_total + feta_total + bread_total
    
    result = total_spent
    return result

print(solution())