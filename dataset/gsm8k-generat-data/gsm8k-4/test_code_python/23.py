def solution():
    """Ann's favorite store was having a summer clearance. For $75 she bought 5 pairs of shorts for $7 each and 2 pairs of shoes for $10 each. She also bought 4 tops, all at the same price. How much did each top cost?"""
    # Define the total amount spent and the prices of the shorts and shoes
    total_spent = 75
    shorts_price = 7
    shoes_price = 10

    # Calculate the total amount spent on the shorts and the shoes
    shorts_spent = 5 * shorts_price
    shoes_spent = 2 * shoes_price

    # Calculate the amount spent on the tops
    tops_spent = total_spent - shorts_spent - shoes_spent

    # Calculate the price of each top
    top_price = tops_spent / 4

    # Return the result
    result = top_price
    return result

print(solution())