def solution():
    """John decides to start collecting art. He pays the same price for his first 3 pieces of art and the total price came to $45,000. The next piece of art was 50% more expensive than those. How much did all the art cost?"""
    # Define the total number of pieces of art
    total_pieces = 4

    # Calculate the price of the first 3 pieces of art
    first_three_price = 45000 / 3

    # Calculate the price of the fourth piece of art
    fourth_price = first_three_price * 1.5

    # Calculate the total cost of all the pieces of art
    total_cost = first_three_price * 3 + fourth_price

    # return the result
    result = total_cost
    return result

print(solution())