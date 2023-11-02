def solution():
    """With her savings, Sara bought two books: a book for 5.5£ and a book for 6.5£. She gives a 20£ bill to the seller. How much change does she get back?"""
    book1_price = 5.5
    book2_price = 6.5
    total_price = book1_price + book2_price
    payment = 20
    change = payment - total_price
    result = change
    return result

print(solution())