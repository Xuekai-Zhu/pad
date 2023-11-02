def solution():
    """Iris went to the mall to buy clothes.  She bought three jackets at $10 each, two pairs of shorts at $6 each, and four pairs of pants at $12 each. How much did she spend in all?"""
    # Define the prices of the jackets, shorts, and pants
    jacket_price = 10
    shorts_price = 6
    pants_price = 12

    # Calculate the total cost of the jackets
    total_jackets_cost = 3 * jacket_price

    # Calculate the total cost of the shorts
    total_shorts_cost = 2 * shorts_price

    # Calculate the total cost of the pants
    total_pants_cost = 4 * pants_price

    # Calculate the total cost of all the clothes
    total_cost = total_jackets_cost + total_shorts_cost + total_pants_cost

    # return the result
    result = total_cost
    return result

print(solution())