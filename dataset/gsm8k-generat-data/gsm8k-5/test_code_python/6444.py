def solution():
    starting_stock = 800  # Ali had 800 books in his stock
    books_sold = 60 + 10 + 20 + 44 + 66  # Ali sold a total of these many books
    books_not_sold = starting_stock - books_sold  # Calculate the number of books not sold
    result = books_not_sold
    return result

print(solution())