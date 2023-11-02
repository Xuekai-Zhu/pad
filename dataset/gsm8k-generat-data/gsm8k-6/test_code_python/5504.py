def solution():
    books = 200
    book_price = 1.5
    record_cost = 3
    num_records = 75

    # Calculate the total amount of money Thomas makes from selling his books
    total_money_from_books = books * book_price

    # Calculate the total cost of buying the records
    total_cost_of_records = num_records * record_cost

    # Calculate the amount of money Thomas has left over after buying the records
    money_left_over = total_money_from_books - total_cost_of_records
    result = money_left_over
    return result

print(solution())