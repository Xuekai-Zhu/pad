def solution():
    """Tara is saving up to buy a new clarinet. She already has $10 saved. The clarinet costs $90. She plans to sell her old books to make the money. She sells each book of hers for $5. However, when she is halfway towards her goal, she loses all her savings and has to start over. How many books does she sell in total by the time she reaches her goal?"""
    initial_savings = 10
    clarinet_cost = 90
    selling_price = 5
    books_needed = (clarinet_cost - initial_savings) // selling_price
    total_books = books_needed

    # if Tara loses her savings halfway
    if initial_savings + (books_needed * selling_price) >= (clarinet_cost // 2):
        second_try_books_needed = (clarinet_cost - initial_savings - (books_needed * selling_price)) // selling_price
        total_books = books_needed + second_try_books_needed

    result = total_books
    return result

print(solution())