def solution():
    
    # Define the initial number of books and the sales price per book
    INITIAL_BOOKS = 250
    BOOK_PRICE = 20

    # Calculate the total sales in the first year
    first_year_sales = INITIAL_BOOKS * BOOK_PRICE * 2

    # Calculate the total sales in the second year
    second_year_sales = (INITIAL_BOOKS - 50) * BOOK_PRICE + 45

    # Display the total sales in the second year
    result = second_year_sales
    return result

print(solution())