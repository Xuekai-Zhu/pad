def solution():
    """Pearl wants to order 5 monogrammed Christmas stockings for each of her 5 grandchildren and her own 4 children.  The stockings are $20.00 each and currently 10% off.  The monogramming will costs $5.00 per stocking.  How much will the stockings costs?"""
    # Define the cost and discount of each stocking
    STOCKING_PRICE = 20
    DISCOUNT_PERCENTAGE = 10

    # Define the number of stockings for each child and grandchild
    CHILDREN_STOCKINGS = 5
    GRANDCHILDREN_STOCKINGS = 5

    # Calculate the total number of stockings
    total_stockings = CHILDREN_STOCKINGS * 4 + GRANDCHILDREN_STOCKINGS * 5

    # Calculate the cost of the stockings before discount
    cost_before_discount = total_stockings * STOCKING_PRICE

    # Calculate the amount of discount
    discount = cost_before_discount * DISCOUNT_PERCENTAGE / 100

    # Calculate the cost of the monogramming
    monogramming_cost = total_stockings * 5

    # Calculate the total cost of the stockings
    total_cost = cost_before_discount - discount + monogramming_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())