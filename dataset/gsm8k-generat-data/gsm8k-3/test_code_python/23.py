def solution():
    """Ann's favorite store was having a summer clearance. For $75 she bought 5 pairs of shorts for $7 each and 2 pairs of shoes for $10 each. She also bought 4 tops, all at the same price. How much did each top cost?"""
    # Define the prices of the shorts and shoes
    short_price = 7
    shoe_price = 10

    # Calculate the total cost of the shorts and shoes
    shorts_cost = 5 * short_price
    shoes_cost = 2 * shoe_price

    # Calculate the total amount spent on shorts, shoes, and tops
    total_spent = 75
    top_cost = (total_spent - shorts_cost - shoes_cost) / 4

    # return the result
    result = top_cost
    return result

print(solution())