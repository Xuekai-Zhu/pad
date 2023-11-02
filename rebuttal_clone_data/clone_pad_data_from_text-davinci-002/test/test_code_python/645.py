def solution():
    money_given = 48
    book_cost = 2
    books_bought = 5
    money_spent = books_bought * book_cost
    money_left = money_given - money_spent
    result = money_left
    return result

print(solution())