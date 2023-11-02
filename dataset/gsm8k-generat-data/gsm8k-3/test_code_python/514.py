def solution():
    """Clara brings a package of 100 stickers to school. She gives 10 stickers to a boy she likes. She gives half of the stickers which she has left to her best friends. How many stickers does Clara have left?"""
    # Define the initial number of stickers
    num_stickers = 100

    # Give 10 stickers to the boy she likes
    num_stickers -= 10

    # Give half of the remaining stickers to her best friends
    num_stickers /= 2

    # Display the remaining number of stickers
    result = num_stickers
    return result

print(solution())