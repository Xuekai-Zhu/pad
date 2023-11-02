def solution():
    
    # Define the cost per book and the flat fee
    COST_PER_BOOK = 0.5
    FLAT_FEE = 2.0

    # Define the number of books owed
    books_owed = 8

    # Calculate the total cost of the overdue books
    overdue_cost = (books_owed * COST_PER_BOOK) + FLAT_FEE

    # Calculate the total cost of the overdue books
    total_cost = overdue_cost + 2

    # Display the total cost
    result = total_cost
    return result

print(solution())