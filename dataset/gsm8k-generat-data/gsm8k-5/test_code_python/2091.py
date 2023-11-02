def solution():
    original_price = 184  # Shara paid $184 for a pair of shoes
    discount_rate = 0.08  # The store has an 8% discount on all items

    # Calculate the discount amount
    discount_amount = original_price * discount_rate

    # Calculate the final price after the discount
    final_price = original_price - discount_amount

    # Calculate the amount Shara saved
    amount_saved = original_price - final_price
    result = amount_saved
    return result

print(solution())