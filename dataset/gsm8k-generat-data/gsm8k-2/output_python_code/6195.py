def solution():
    """Vanessa's new business is thriving and she frequently has orders to post. She has run out of packing peanuts for the packages and is now wondering how many orders she has sent. Each large order needs 200g of packing peanuts while small orders need just 50g of packing peanuts. If Lisa has used a total of 800g of packing peanuts and she knows she has sent 3 large orders, how many small orders has Lisa sent?"""
    large_order_peanuts = 200
    small_order_peanuts = 50
    total_peanuts_used = 800
    total_large_orders = 3
    peanuts_from_large_orders = total_large_orders * large_order_peanuts
    peanuts_from_small_orders = total_peanuts_used - peanuts_from_large_orders
    number_of_small_orders = peanuts_from_small_orders / small_order_peanuts
    result = number_of_small_orders
    return result

print(solution())