def solution():
    """Wilson goes to a fast-food restaurant. He buys 2 hamburgers for $5 each and 3 bottles of cola for $2 each. Wilson uses his $4 discount coupon. How much money does he pay in total?"""
    # Define the prices of hamburgers and cola
    hamburger_price = 5
    cola_price = 2

    # Calculate the total cost before discount
    total_cost_before_discount = (2 * hamburger_price) + (3 * cola_price)

    # Apply the discount
    total_cost_after_discount = total_cost_before_discount - 4

    # return the result
    result = total_cost_after_discount
    return result

print(solution())