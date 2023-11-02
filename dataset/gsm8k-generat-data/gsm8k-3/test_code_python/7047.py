def solution():
    """Iris went to the mall to buy clothes.  She bought three jackets at $10 each, two pairs of shorts at $6 each, and four pairs of pants at $12 each. How much did she spend in all?"""
    # Define the prices of each item
    JACKET_PRICE = 10
    SHORTS_PRICE = 6
    PANTS_PRICE = 12

    # Define the quantity of each item purchased
    jackets = 3
    shorts = 2
    pants = 4

    # Calculate the total cost of the jackets
    jacket_cost = jackets * JACKET_PRICE

    # Calculate the total cost of the shorts
    shorts_cost = shorts * SHORTS_PRICE

    # Calculate the total cost of the pants
    pants_cost = pants * PANTS_PRICE

    # Calculate the total cost of all the clothes
    total_cost = jacket_cost + shorts_cost + pants_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())