def solution():
    """Simon wanted to buy flowers that his mom could plant for Mother's Day. The garden center was offering 10% off all purchases. He bought 5 pansies at $2.50 each, one hydrangea that cost $12.50 and 5 petunias that cost $1.00 each. If he paid with a $50 bill, how much change would Simon receive back from his purchase?"""
    # Define the prices of each type of flower
    pansy_price = 2.50
    hydrangea_price = 12.50
    petunia_price = 1.00

    # Calculate the total cost of all the flowers before the discount
    total_cost = (5 * pansy_price) + hydrangea_price + (5 * petunia_price)

    # Calculate the discount
    discount = total_cost * 0.10

    # Calculate the total cost after the discount
    total_cost_discounted = total_cost - discount

    # Calculate the amount of change Simon would receive from a $50 bill
    change = 50 - total_cost_discounted

    # return the result
    result = change
    return result

print(solution())