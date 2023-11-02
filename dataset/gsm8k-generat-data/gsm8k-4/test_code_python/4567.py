def solution():
    """A local bookshop is selling off its old inventory in order to bring in newer books. They currently have 743 books in their store. They sold 37 books in-store on Saturday and sold 128 books online. On Sunday, they sold twice as many books in-store and increased their online sales by 34 books. They also received a shipment of 160 books. How many books do they currently have?"""
    # Define the initial number of books
    initial_books = 743

    # Calculate the number of books sold and add the new shipment
    books_sold = 37 + 128 + (2 * 37) + (128 + 34)
    new_shipment = 160
    total_books = initial_books - books_sold + new_shipment

    # return the result
    result = total_books
    return result

print(solution())