def solution():
    """Rita bought 5 short dresses, 3 pairs of pants and 4 jackets from a store that sells second-hand clothes. The dresses cost $20 each, the pants cost $12, the jackets cost $30 each, and she spent an additional $5 on transportation. If she had $400 initially, how much does she have now?"""
    # Define the prices of dresses, pants, and jackets
    dress_price = 20
    pant_price = 12
    jacket_price = 30

    # Calculate the total cost of the purchases
    total_cost = (5 * dress_price) + (3 * pant_price) + (4 * jacket_price) + 5

    # Calculate the amount of money Rita has left
    remaining_money = 400 - total_cost

    # Return the result
    result = remaining_money
    return result

print(solution())