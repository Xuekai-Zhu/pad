def solution():
    """Kenny charges $15 per lawn, and plans to use the profits to buy video-games and books. The video-games are $45 each and the books are $5 each. He has mowed 35 lawns and wants to buy 5 video-games, how many books can he buy?"""
    # Define the price of each lawn, video-game, and book
    LAWN_PRICE = 15
    VIDEO_GAME_PRICE = 45
    BOOK_PRICE = 5

    # Calculate Kenny's earnings from mowing lawns
    lawn_earnings = LAWN_PRICE * 35

    # Calculate the cost of the video-games
    video_game_cost = VIDEO_GAME_PRICE * 5

    # Calculate Kenny's remaining earnings after buying the video-games
    remaining_earnings = lawn_earnings - video_game_cost

    # Calculate the number of books Kenny can buy
    books_bought = remaining_earnings // BOOK_PRICE

    # Display the number of books Kenny can buy
    result = books_bought
    return result

print(solution())