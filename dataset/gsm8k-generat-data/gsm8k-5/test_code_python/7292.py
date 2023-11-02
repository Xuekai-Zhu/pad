def solution():
    # Calculate the cost of the five textbooks bought on sale
    sale_books_cost = 5 * 10  # 5 textbooks for $10 each

    # Calculate the cost of the two textbooks ordered online
    online_books_cost = 40

    # Calculate the cost of the three textbooks bought from the bookstore
    bookstore_books_cost = 3 * online_books_cost * 3  # Three times the cost of the online ordered books

    # Calculate the total cost of all textbooks
    total_cost = sale_books_cost + online_books_cost + bookstore_books_cost
    result = total_cost
    return result

print(solution())