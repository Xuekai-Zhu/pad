def solution():
    original_price = 12
    num_cards = 10
    discount = 2

    # Calculate the total cost of all cards without discount
    total_cost = original_price * num_cards

    # Calculate the total discount given to Ivan
    total_discount = discount * num_cards

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost - total_discount
    result = total_cost_after_discount
    return result

print(solution())