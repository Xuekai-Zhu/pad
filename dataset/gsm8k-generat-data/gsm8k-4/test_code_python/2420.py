def solution():
    """While on vacation in Hawaii, Steve and Georgia decided to ship pineapples to their home. Each pineapple costs $1.25 and they buy a dozen. It will cost $21.00 to ship all of them to their home. How much will each pineapple end up costing them?"""
    # Define the cost per pineapple and the number of pineapples
    pineapple_cost = 1.25
    pineapple_count = 12

    # Calculate the total cost of the pineapples
    total_pineapple_cost = pineapple_cost * pineapple_count

    # Calculate the cost per pineapple including shipping
    total_cost = total_pineapple_cost + 21
    cost_per_pineapple = total_cost / pineapple_count

    # return the result
    result = round(cost_per_pineapple, 2)
    return result

print(solution())