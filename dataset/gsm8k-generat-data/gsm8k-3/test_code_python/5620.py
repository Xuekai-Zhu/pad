def solution():
    """To make room for a new inventory of books, Gordon's local bookstore is offering 30% off any book that is over $22.00 and 20% off any book under $20.00.  He buys several books with the following prices; $25.00, $18.00, $21.00, $35.00, $12.00 and $10.00.  How much will he spend on books?"""
    # Define the discount percentages for books over and under $22
    OVER_22_DISCOUNT = 0.3
    UNDER_20_DISCOUNT = 0.2

    # Define the prices of each book
    book_prices = [25, 18, 21, 35, 12, 10]

    # Initialize the total cost of the books
    total_cost = 0

    # Calculate the discount and total cost for each book
    for price in book_prices:
        if price > 22:
            discount = price * OVER_22_DISCOUNT
            total_cost += price - discount
        elif price < 20:
            discount = price * UNDER_20_DISCOUNT
            total_cost += price - discount
        else:
            total_cost += price

    # Display the total cost of the books
    result = total_cost
    return result

print(solution())