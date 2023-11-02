def solution():
    clarinet_cost = 90
    money_saved = 10
    book_sale_price = 5
    money_needed = clarinet_cost - money_saved
    number_of_books_sold = money_needed / book_sale_price
    result = number_of_books_sold
    return result

print(solution())