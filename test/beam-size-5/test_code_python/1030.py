def solution():
    
    # Define the cost of each item
    BOOK_COST = 16
    PENCIL_COST = 6

    # Define the number of each item purchased
    num_books = 3
    num_pencils = 3

    # Calculate the total cost of the books
    book_cost = num_books * BOOK_COST

    # Calculate the total cost of the pencils
    pencil_cost = num_pencils * PENCIL_COST

    # Calculate the total cost
    total_cost = book_cost + pencil_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())