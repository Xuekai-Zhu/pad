def solution():
    """Colton had 72 dolphin stickers. He gave 4 stickers each to 3 friends. He also gave his friend Mandy 2 more than he gave his three friends total. And he gave Justin 10 less than Mandy. How many stickers does Colton have left?"""
    # Define the initial number of dolphin stickers
    initial_stickers = 72

    # Define the number of stickers given to each friend
    friend_stickers = 4

    # Calculate the total number of stickers given to the three friends
    total_friend_stickers = friend_stickers * 3

    # Calculate the number of stickers given to Mandy
    mandy_stickers = total_friend_stickers + 2

    # Calculate the number of stickers given to Justin
    justin_stickers = mandy_stickers - 10

    # Calculate the total number of stickers given away
    total_given_away = total_friend_stickers + mandy_stickers + justin_stickers

    # Calculate the number of stickers left with Colton
    stickers_left = initial_stickers - total_given_away

    # return the result
    result = stickers_left
    return result

print(solution())