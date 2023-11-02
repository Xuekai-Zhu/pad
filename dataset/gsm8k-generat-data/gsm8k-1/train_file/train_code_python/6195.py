def solution():
    """Vanessa's new business is thriving and she frequently has orders to post. She has run out of packing peanuts for the packages and is now wondering how many orders she has sent. Each large order needs 200g of packing peanuts while small orders need just 50g of packing peanuts. If Lisa has used a total of 800g of packing peanuts and she knows she has sent 3 large orders, how many small orders has Lisa sent?"""
    large_order_peanuts = 200
    small_order_peanuts = 50
    total_peanuts = 800
    num_large_orders = 3
    peanuts_used_in_large_orders = large_order_peanuts * num_large_orders
    peanuts_used_in_small_orders = total_peanuts - peanuts_used_in_large_orders
    num_small_orders = peanuts_used_in_small_orders / small_order_peanuts
    result = num_small_orders
    return result

print(solution())