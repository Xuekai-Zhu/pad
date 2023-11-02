def solution():
    initial_money = 236  # Fred had 236 dollars to spend
    final_money = 14  # After buying the books, he had 14 dollars left
    num_books = 6  # Fred bought 6 books

    # Calculate the total cost of the books
    total_cost = initial_money - final_money
    book_cost = total_cost / num_books  # Calculate the cost of each book

    result = book_cost
    return result

print(solution())