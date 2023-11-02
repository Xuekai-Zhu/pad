def solution():
    """To make room for a new inventory of books, Gordon's local bookstore is offering 30% off any book that is over $22.00 and 20% off any book under $20.00. He buys several books with the following prices; $25.00, $18.00, $21.00, $35.00, $12.00 and $10.00. How much will he spend on books?"""
    # Define the prices of each book
    book_prices = [25, 18, 21, 35, 12, 10]

    # Calculate the total cost of books over $22 with the discount
    books_over_22 = [price * 0.7 for price in book_prices if price > 22]
    total_cost_over_22 = sum(books_over_22)

    # Calculate the total cost of books under $20 with the discount
    books_under_20 = [price * 0.8 for price in book_prices if price < 20]
    total_cost_under_20 = sum(books_under_20)

    # Calculate the total cost of books between $20 and $22 without discount
    books_between_20_22 = [price for price in book_prices if 20 <= price <= 22]
    total_cost_between_20_22 = sum(books_between_20_22)

    # Calculate the total cost of all books
    total_cost = total_cost_over_22 + total_cost_under_20 + total_cost_between_20_22

    # Return the result
    result = total_cost
    return result

print(solution())