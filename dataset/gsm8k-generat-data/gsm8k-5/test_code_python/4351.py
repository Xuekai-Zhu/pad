def solution():
    # Calculate the total cost of notebooks and books
    total_notebook_cost = 7 * 4
    total_book_cost = 2 * 7
    total_cost = total_notebook_cost + total_book_cost

    # Calculate the money Joe has left
    money_left = 56 - total_cost
    result = money_left
    return result

print(solution())