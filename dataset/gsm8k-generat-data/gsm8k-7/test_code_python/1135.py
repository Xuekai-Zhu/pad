def solution():
    initial_money = 48
    num_books = 5
    book_price = 2

    # Calculate the total cost of all books
    total_books_cost = num_books * book_price

    # Calculate how much money Reggie has left
    money_left = initial_money - total_books_cost
    result = money_left
    return result

print(solution())