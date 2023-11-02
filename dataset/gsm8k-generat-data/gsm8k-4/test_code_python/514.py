def solution():
    """Clara brings a package of 100 stickers to school. She gives 10 stickers to a boy she likes. She gives half of the stickers which she has left to her best friends. How many stickers does Clara have left?"""
    # Define the initial number of stickers
    initial_stickers = 100

    # Subtract the stickers given to the boy
    stickers_left = initial_stickers - 10

    # Calculate the number of stickers to give to friends
    stickers_friends = stickers_left / 2

    # Calculate the number of stickers left after giving to friends
    stickers_left = stickers_left - stickers_friends

    result = stickers_left
    return result

print(solution())