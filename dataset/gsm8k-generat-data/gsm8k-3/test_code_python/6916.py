def solution():
    """A store marks a book 30% above the cost. But during a sale, a 10% discount was given. If the book costs $50, what is the percent profit?"""
    # Define the original cost of the book
    cost = 50

    # Calculate the selling price of the book with the markup
    markup_percentage = 30
    selling_price = cost * (1 + markup_percentage / 100)

    # Calculate the selling price of the book with the discount
    discount_percentage = 10
    final_selling_price = selling_price * (1 - discount_percentage / 100)

    # Calculate the profit percentage
    profit_percentage = (final_selling_price - cost) / cost * 100

    # Display the profit percentage
    result = profit_percentage
    return result

print(solution())