def solution():
    profit = 120  # Tina has made a $120 profit on her sales
    cost_per_book = 5  # Each book costs $5 to make
    selling_price_per_book = 20  # Tina sells each book for $20
    books_sold = (profit / (selling_price_per_book - cost_per_book)) / 2  # Calculate the number of books sold
    result = books_sold
    return result

print(solution())