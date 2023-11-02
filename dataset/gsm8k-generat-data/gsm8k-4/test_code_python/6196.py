def solution():
    """Vanessa's new business is thriving and she frequently has orders to post. She has run out of packing peanuts for the packages and is now wondering how many orders she has sent. Each large order needs 200g of packing peanuts while small orders need just 50g of packing peanuts. If Lisa has used a total of 800g of packing peanuts and she knows she has sent 3 large orders, how many small orders has Lisa sent?"""
    # Define the weight of packing peanuts for each type of order
    LARGE_ORDER_WEIGHT = 200
    SMALL_ORDER_WEIGHT = 50

    # Define the total weight of packing peanuts used and the number of large orders sent
    total_weight = 800
    large_orders = 3

    # Calculate the weight of packing peanuts used for large orders
    large_weight = large_orders * LARGE_ORDER_WEIGHT

    # Calculate the weight of packing peanuts used for small orders
    small_weight = total_weight - large_weight

    # Calculate the number of small orders sent
    small_orders = small_weight // SMALL_ORDER_WEIGHT

    # return the result
    result = small_orders
    return result

print(solution())