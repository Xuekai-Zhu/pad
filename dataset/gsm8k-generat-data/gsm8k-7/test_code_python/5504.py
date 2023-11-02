def solution():
    num_books = 200
    book_price = 1.5

    num_records = 75
    record_price = 3

    # Calculate the total amount of money Thomas earns from selling his books
    total_earnings = num_books * book_price

    # Calculate the total cost of buying 75 records
    total_cost = num_records * record_price

    # Calculate the remaining amount of money Thomas has after buying the records
    remaining_money = total_earnings - total_cost
    result = remaining_money
    return result

print(solution())