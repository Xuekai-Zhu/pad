def solution():
    """While on vacation in Hawaii, Steve and Georgia decided to ship pineapples to their home.  Each pineapple costs $1.25 and they buy a dozen.  It will cost $21.00 to ship all of them to their home.  How much will each pineapple end up costing them?"""
    # Define the cost of each pineapple and the cost of shipping
    PINEAPPLE_PRICE = 1.25
    SHIPPING_COST = 21.00

    # Define the number of pineapples bought
    pineapples_bought = 12

    # Calculate the total cost of the pineapples and shipping
    total_cost = (pineapples_bought * PINEAPPLE_PRICE) + SHIPPING_COST

    # Calculate the cost per pineapple by dividing the total cost by the number of pineapples bought
    cost_per_pineapple = total_cost / pineapples_bought

    # Display the cost per pineapple
    result = cost_per_pineapple
    return result

print(solution())