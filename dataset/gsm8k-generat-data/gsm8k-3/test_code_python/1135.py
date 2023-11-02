def solution():
    """Reggie's father gave him $48. Reggie bought 5 books, each of which cost $2. How much money does Reggie have left?"""
    # Define the amount of money Reggie's father gave him
    initial_money = 48

    # Define the price of each book
    book_price = 2

    # Calculate the total cost of the books
    total_book_cost = book_price * 5

    # Calculate the money left after buying the books
    money_left = initial_money - total_book_cost

    # Display the remaining money
    result = money_left
    return result

print(solution())