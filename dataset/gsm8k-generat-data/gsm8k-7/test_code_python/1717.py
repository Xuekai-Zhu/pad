def solution():
    original_price = 40
    num_pairs = 3

    # Calculate the number of pairs eligible for the discount
    num_pairs_discounted = num_pairs // 2

    # Calculate the total cost of all pairs of jeans without discount
    total_cost_before_discount = original_price * num_pairs

    # Calculate the total discount amount
    total_discount_amount = original_price * 0.1 * num_pairs_discounted

    # Calculate the total cost of all pairs of jeans with discount
    total_cost_after_discount = total_cost_before_discount - total_discount_amount

    result = total_cost_after_discount
    return result

print(solution())