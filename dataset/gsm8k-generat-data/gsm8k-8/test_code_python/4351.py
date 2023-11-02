def solution():
    # Calculate the total cost of notebooks
    notebook_cost = 7 * 4

    # Calculate the total cost of books
    book_cost = 2 * 7

    # Calculate the total spent
    total_spent = notebook_cost + book_cost

    # Calculate the amount of money left
    money_left = 56 - total_spent
    result = money_left
    return result

print(solution())