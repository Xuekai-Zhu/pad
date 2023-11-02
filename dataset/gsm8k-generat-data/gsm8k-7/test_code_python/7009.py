def solution():
    candy_cost = 15
    leftover_money = 3
    pages_per_book = 150

    # Calculate the total amount of money earned from reading books
    total_money_earned = (candy_cost + leftover_money) * 100  # convert to cents
    num_books_read = total_money_earned // (pages_per_book * 1)  # convert to cents

    result = num_books_read
    return result

print(solution())