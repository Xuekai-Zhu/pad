def solution():
    """Zander collected 100 stickers. He gave some of his stickers to his two friends, Andrew and Bill. Andrew received 1/5 of Zander's stickers, while Bill received 3/10 of the remaining stickers. How many stickers did Andrew give to his two friends?"""
    # Define the number of stickers Zander collected
    total_stickers = 100

    # Calculate the number of stickers Andrew received
    andrew_stickers = total_stickers * 1/5

    # Calculate the number of stickers Bill received
    bill_stickers = (total_stickers - andrew_stickers) * 3/10

    # Calculate the number of stickers Zander gave to both friends
    zander_gave = andrew_stickers + bill_stickers

    # Calculate the number of stickers Andrew gave to both friends
    andrew_gave = total_stickers - zander_gave

    # Display the number of stickers Andrew gave to both friends
    result = andrew_gave
    return result

print(solution())