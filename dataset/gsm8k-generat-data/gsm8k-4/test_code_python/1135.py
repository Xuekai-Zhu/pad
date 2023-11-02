def solution():
    """Reggie's father gave him $48. Reggie bought 5 books, each of which cost $2. How much money does Reggie have left?"""
    # Define the initial amount of money Reggie has
    initial_money = 48

    # Define the cost of each book
    book_cost = 2

    # Calculate the total cost of the books
    total_book_cost = book_cost * 5

    # Calculate the amount of money left after buying the books
    money_left = initial_money - total_book_cost

    # return the result
    result = money_left
    return result

print(solution())