def solution():
    """John decides to start collecting art.  He pays the same price for his first 3 pieces of art and the total price came to $45,000.  The next piece of art was 50% more expensive than those.  How much did all the art cost?"""
    # Define the price of the first 3 pieces
    price_first_3 = 45000/3

    # Define the price of the fourth piece
    price_fourth = price_first_3 * 1.5

    # Calculate the total cost of all the art
    total_cost = price_first_3 * 3 + price_fourth

    # Display the total cost
    result = total_cost
    return result

print(solution())