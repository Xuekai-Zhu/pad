def solution():
    books_sold_tue = 7
    books_sold_wed = 3 * books_sold_tue
    books_sold_thu = 3 * books_sold_wed

    total_books_sold = books_sold_tue + books_sold_wed + books_sold_thu
    result = total_books_sold
    return result

print(solution())