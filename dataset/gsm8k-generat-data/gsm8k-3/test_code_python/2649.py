def solution():
    """ In a store, an Uno Giant Family Card costs $12. When Ivan bought ten pieces, he was given a discount of $2 each. How much did Ivan pay in all?"""
    # Define the cost of each Uno Giant Family Card and the discount
    CARD_COST = 12
    DISCOUNT = 2

    # Define the number of Uno Giant Family Cards purchased
    num_cards = 10

    # Calculate the total cost before the discount
    total_cost_before_discount = num_cards * CARD_COST

    # Calculate the total discount
    total_discount = num_cards * DISCOUNT

    # Calculate the total cost after the discount
    total_cost_after_discount = total_cost_before_discount - total_discount

    # Display the total cost after the discount
    result = total_cost_after_discount
    return result

print(solution())