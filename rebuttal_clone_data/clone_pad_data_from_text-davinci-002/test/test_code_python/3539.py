def solution():

    total_items = 400
    book_ratio = 7
    pen_ratio = 3
    book_total = total_items * (book_ratio / (book_ratio + pen_ratio))
    
    result = book_total
    
    return book_total

print(solution())