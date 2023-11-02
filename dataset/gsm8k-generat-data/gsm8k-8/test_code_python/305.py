def solution():
    # Define the number of books Tommy wants to buy
    num_books = 8

    # Define the cost of one book
    book_cost = 5

    # Define the amount of money Tommy already has
    current_money = 13

    # Calculate the total cost of all the books
    total_cost = num_books * book_cost

    # Calculate the amount of money Tommy needs to save up
    amount_to_save = total_cost - current_money
    result = amount_to_save
    return result

print(solution())