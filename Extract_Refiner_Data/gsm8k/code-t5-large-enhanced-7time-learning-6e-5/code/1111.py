def solution():
    
    # Define the initial budget and the amount spent
    initial_budget = 16
    amount_spent = 4

    # Define the number of books purchased today
    num_books = 2

    # Define the remaining budget after purchasing the books
    remaining_budget = initial_budget - amount_spent

    # Calculate the cost of the books purchased today
    book_cost = remaining_budget / num_books

    # Display the cost of each book
    result = book_cost
    return result

print(solution())