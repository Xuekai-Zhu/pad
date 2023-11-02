def solution():
    total_books = 10  # Lovely has a total of 10 books to sell
    sale_price1 = 2.50  # Lovely sells 2/5 of her books at $2.50 each
    sale_price2 = 2  # Lovely sells the remaining 3/5 of her books at $2 each

    # Calculate the number of books sold at $2.50 each
    num_books1 = int(total_books * 2 / 5)
    total_money1 = num_books1 * sale_price1

    # Calculate the number of books sold at $2 each
    num_books2 = total_books - num_books1
    total_money2 = num_books2 * sale_price2

    # Calculate the total amount earned by Lovely
    total_money = total_money1 + total_money2
    result = total_money
    return result

print(solution())