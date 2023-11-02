def solution():
    snack_fee = 150 * 6  # Each member pays $150 for snacks
    hard_book_fee = 30 * 6  # Each member pays $30 for 6 hardcover books
    paper_book_fee = 12 * 6  # Each member pays $12 for 6 paperback books

    # Calculate the total amount of money collected by Niles
    total_fee = snack_fee + hard_book_fee + paper_book_fee
    result = total_fee
    return result

print(solution())