def solution():
    """Pearl wants to order 5 monogrammed Christmas stockings for each of her 5 grandchildren and her own 4 children. The stockings are $20.00 each and currently 10% off. The monogramming will costs $5.00 per stocking. How much will the stockings costs?"""
    # Define the number of stockings to be ordered
    num_stockings = 5 * 5 + 4

    # Define the original price per stocking
    original_price = 20.00

    # Calculate the discounted price per stocking
    discounted_price = original_price * 0.9

    # Calculate the total cost of stockings before adding monogramming
    total_cost_no_monogram = num_stockings * discounted_price

    # Calculate the total cost of monogramming
    total_cost_monogram = num_stockings * 5.00

    # Add the two costs to get the total cost of stockings with monogramming
    total_cost = total_cost_no_monogram + total_cost_monogram

    result = total_cost
    return result

print(solution())