def solution():
    """Niles is collecting his book club's annual fees. Each of the six members pays $150/year towards snacks, plus $30 each for six hardcover books and $12 each for six paperback books. How much money does Niles collect in total?"""
    snacks_fee = 150 * 6
    hardcover_books_fee = 30 * 6
    paperback_books_fee = 12 * 6
    total_fee = snacks_fee + hardcover_books_fee + paperback_books_fee
    result = total_fee
    return result

print(solution())