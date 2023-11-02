def solution():
    """The price of a book was $400. If the book's price is decreased by 15% and then increased by 40%, what is the final price of the book?"""
    # Define the initial price of the book
    initial_price = 400

    # Calculate the price after the first decrease
    price_after_decrease = initial_price * 0.85

    # Calculate the final price after the increase
    final_price = price_after_decrease * 1.4

    result = final_price
    return result

print(solution())