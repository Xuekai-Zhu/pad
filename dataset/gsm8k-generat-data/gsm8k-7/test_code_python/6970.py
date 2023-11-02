def solution():
    friends_stuffed = 18
    friends_action = 42
    board_games = 2
    puzzles = 13
    total_donated = 108

    # Calculate the number of toys donated by Joel's sister
    sister_toys = total_donated - (friends_stuffed + friends_action + board_games + puzzles)

    # Calculate the number of toys Joel donated
    joel_toys = (sister_toys + board_games + puzzles) * 2

    result = joel_toys
    return result

print(solution())