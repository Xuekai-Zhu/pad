def solution():
    
    num_books = 200
    book_price = 1.5
    record_price = 3
    num_records = 75
    total_book_sales = num_books * book_price
    total_record_cost = num_records * record_price
    money_left = total_book_sales - total_record_cost
    result = money_left
    return result

print(solution())