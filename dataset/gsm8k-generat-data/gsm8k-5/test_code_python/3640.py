def solution():
    card_value = 0.05  # Each basketball card is worth 5 cents
    comic_cost = 6  # Each comic book costs $6

    # Calculate the total amount earned from selling the basketball cards
    total_card_value = card_value * 2000

    # Calculate the maximum number of comic books that can be bought
    max_comic_books = int(total_card_value / comic_cost)

    # Calculate the amount spent on buying comic books
    total_comic_cost = max_comic_books * comic_cost

    # Calculate the leftover money
    leftover_money = total_card_value - total_comic_cost
    result = leftover_money
    return result

print(solution())