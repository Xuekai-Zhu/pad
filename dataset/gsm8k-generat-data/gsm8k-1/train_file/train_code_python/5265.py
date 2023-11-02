def solution():
    """Kenny plans to mow lawns all summer, and then use the profits to buy video-games and books. He charges $15 per lawn. The video-games are $45 each. The books are $5 each. At the end of the summer he has mowed 35 lawns. There are 5 video-games he really wants, and then he will use the rest for books. How many books can he buy?"""
    lawn_price = 15
    games_price = 45
    books_price = 5
    num_lawns = 35
    total_earned = num_lawns * lawn_price
    games_cost = games_price * 5
    book_money = total_earned - games_cost
    num_books = book_money // books_price
    result = num_books
    return result

print(solution())