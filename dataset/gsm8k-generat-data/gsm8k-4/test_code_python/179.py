def solution():
    """Colton had 72 dolphin stickers. He gave 4 stickers each to 3 friends. He also gave his friend Mandy 2 more than he gave his three friends total. And he gave Justin 10 less than Mandy. How many stickers does Colton have left?"""
    # Define the initial number of stickers
    initial_stickers = 72

    # Calculate the number of stickers given to 3 friends
    stickers_given_friends = 4 * 3

    # Calculate the number of stickers given to Mandy
    stickers_given_mandy = stickers_given_friends + 2

    # Calculate the number of stickers given to Justin
    stickers_given_justin = stickers_given_mandy - 10

    # Calculate the total number of stickers given away
    total_stickers_given = stickers_given_friends + stickers_given_mandy + stickers_given_justin

    # Calculate the number of stickers left
    stickers_left = initial_stickers - total_stickers_given

    result = stickers_left
    return result

print(solution())