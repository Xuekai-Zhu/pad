def solution():
    
    # Define the initial cost of merchandise and the item
    INITIAL_COST = 85
    ITEM_COST = 15

    # Calculate the cost of the item after returning the item
    item_cost = INITIAL_COST - ITEM_COST

    # Calculate the cost of the frying pan and towels after the discount
    frying_pan_cost = 20 * 0.8
    towels_cost = 30 * 0.9

    # Calculate the new balance on the credit card
    new_balance = item_cost - frying_pan_cost - towels_cost

    # Display the new balance
    result = new_balance
    return result

print(solution())