def solution():
    # Calculate the total value of the card collection
    card_value = 0.05 * 2000

    # Calculate the maximum number of comic books he can buy
    max_comic_books = card_value / 6

    # Calculate how much money he has leftover after buying comic books
    leftover_money = card_value - max_comic_books * 6
    result = leftover_money
    return result

print(solution())