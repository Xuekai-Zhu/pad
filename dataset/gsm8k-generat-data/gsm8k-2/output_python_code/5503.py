def solution():
    """Thomas owns 200 books. He decides to sell them and use the money to buy records. Each book sells for $1.5. A record costs $3. If he buys 75 records, how much money does he have left over?"""
    num_books = 200
    book_price = 1.5
    record_price = 3
    num_records = 75
    total_earnings = num_books * book_price
    total_cost = num_records * record_price
    money_left = total_earnings - total_cost
    result = money_left
    return result

print(solution())