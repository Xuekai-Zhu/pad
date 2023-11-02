def solution():
    initial_stock = 800
    sold_on_monday = 60
    sold_on_tuesday = 10
    sold_on_wednesday = 20
    sold_on_thursday = 44
    sold_on_friday = 66

    # Calculate the total number of books sold
    total_books_sold = sold_on_monday + sold_on_tuesday + sold_on_wednesday + sold_on_thursday + sold_on_friday

    # Calculate the total number of books remaining
    total_books_remaining = initial_stock - total_books_sold
    result = total_books_remaining
    return result

print(solution())