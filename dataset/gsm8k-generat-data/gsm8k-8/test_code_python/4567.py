def solution():
    # Define the initial number of books
    initial_books = 743

    # Calculate the number of books sold on Saturday and Sunday
    sold_instore = 37 + (2*37)
    sold_online = 128 + 34

    # Calculate the total number of books sold
    total_sold = sold_instore + sold_online

    # Calculate the total number of books after the sales and shipment
    total_books = initial_books - total_sold + 160

    result = total_books
    return result

print(solution())