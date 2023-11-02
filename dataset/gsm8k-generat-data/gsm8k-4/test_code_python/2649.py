def solution():
    """In a store, an Uno Giant Family Card costs $12. When Ivan bought ten pieces, he was given a discount of $2 each. How much did Ivan pay in all?"""
    # Define the price of one card and the number of cards purchased
    card_price = 12
    num_cards = 10

    # Calculate the total cost without discount
    total_cost_without_discount = card_price * num_cards

    # Calculate the total cost with discount
    total_cost_with_discount = total_cost_without_discount - (2 * num_cards)

    # Return the result
    result = total_cost_with_discount
    return result

print(solution())