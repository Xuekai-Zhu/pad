def solution():
    current_inventory = 743

    # Calculate the total number of books sold on Saturday
    saturday_sales = 37 + 128

    # Calculate the total number of books sold online on Sunday
    sunday_online_sales = 128 + 34

    # Calculate the total number of books sold in-store on Sunday
    sunday_instore_sales = 2 * 37

    # Calculate the total number of books sold on Sunday
    sunday_sales = sunday_instore_sales + sunday_online_sales

    # Calculate the total number of books received
    books_received = 160

    # Calculate the new inventory after all transactions
    new_inventory = current_inventory - saturday_sales - sunday_sales + books_received 

    result = new_inventory
    return result

print(solution())