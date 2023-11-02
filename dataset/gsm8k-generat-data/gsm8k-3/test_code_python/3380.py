def solution():
    """A bag was originally priced at $500. A week after, the price was reduced by 5%. Since the bag was still not sold, the selling price was reduced by 4% a month after. How much was the total reduction from the original selling price?"""
    # Define the original price of the bag
    original_price = 500

    # Calculate the price after the first reduction
    first_reduction = original_price * 0.05
    price_after_first_reduction = original_price - first_reduction

    # Calculate the price after the second reduction
    second_reduction = price_after_first_reduction * 0.04
    price_after_second_reduction = price_after_first_reduction - second_reduction

    # Calculate the total reduction from the original selling price
    total_reduction = original_price - price_after_second_reduction

    # Display the total reduction
    result = total_reduction
    return result

print(solution())