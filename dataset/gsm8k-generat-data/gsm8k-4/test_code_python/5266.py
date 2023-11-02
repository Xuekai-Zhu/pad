def solution():
    """Kenny plans to mow lawns all summer, and then use the profits to buy video-games and books. He charges $15 per lawn. The video-games are $45 each. The books are $5 each. At the end of the summer he has mowed 35 lawns. There are 5 video-games he really wants, and then he will use the rest for books. How many books can he buy?"""
    # Define the lawn mowing income
    income = 15 * 35

    # Calculate the cost of the video games
    video_games_cost = 45 * 5

    # Calculate the total amount of money available for books
    book_money = income - video_games_cost

    # Calculate the number of books he can buy
    books = book_money // 5

    result = books
    return result

print(solution())