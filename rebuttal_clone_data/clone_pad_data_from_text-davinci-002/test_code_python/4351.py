def solution():
    money_given = 56
    notebook_cost = 4
    book_cost = 7
    notebooks_bought = 7
    books_bought = 2
    total_spent = notebook_cost * notebooks_bought + book_cost * books_bought
    money_left = money_given - total_spent
    result = money_left
    return result

print(solution())