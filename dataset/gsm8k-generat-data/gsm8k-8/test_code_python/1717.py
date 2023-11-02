def solution():
    # Define the original price of one pair of jeans
    original_price = 40
    
    # Define the number of pairs of jeans being bought
    num_pairs = 3

    # Calculate the total cost before discount
    total_before_discount = original_price * num_pairs

    # Calculate the number of pairs that qualify for the discount
    num_discount_pairs = num_pairs // 2

    # Calculate the total discount
    discount_amount = num_discount_pairs * original_price * 0.1

    # Calculate the total cost after discount
    total_after_discount = total_before_discount - discount_amount

    result = total_after_discount
    return result

print(solution())