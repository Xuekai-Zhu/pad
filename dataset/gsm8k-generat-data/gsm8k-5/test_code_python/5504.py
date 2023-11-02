def solution():
    num_books = 200
    book_price = 1.5
    record_price = 3
    num_records = 75
    
    total_money = num_books * book_price
    record_cost = num_records * record_price
    
    remaining_money = total_money - record_cost
    result = remaining_money
    return result

print(solution())