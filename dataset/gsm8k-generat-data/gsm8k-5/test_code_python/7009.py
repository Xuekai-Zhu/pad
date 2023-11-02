def solution():
    pages_per_book = 150  # Pablo reads books that are exactly 150 pages
    candy_cost = 15  # Pablo spends $15 on candy
    leftover_money = 3  # Pablo has $3 leftover after buying candy

    # Calculate the total amount of money Pablo earns from reading books
    total_money = candy_cost + leftover_money
    money_per_book = 0.01 * pages_per_book
    total_books = total_money / money_per_book
    result = int(total_books)
    return result

print(solution())