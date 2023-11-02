def solution():
    total_money = 48  # Reggie's father gave him $48
    num_books = 5  # Reggie bought 5 books
    cost_per_book = 2  # Each book costs $2

    # Calculate the total cost of the books
    total_cost = num_books * cost_per_book

    # Calculate the amount of money Reggie has left
    money_left = total_money - total_cost
    result = money_left
    return result

print(solution())