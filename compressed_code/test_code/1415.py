def solution():
    
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