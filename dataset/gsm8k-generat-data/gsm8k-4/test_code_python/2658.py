def solution():
    """Zander collected 100 stickers. He gave some of his stickers to his two friends, Andrew and Bill. Andrew received 1/5 of Zander's stickers, while Bill received 3/10 of the remaining stickers. How many stickers did Andrew give to his two friends?"""
    # Define the total number of stickers Zander collected
    total_stickers = 100

    # Calculate the number of stickers Andrew received
    andrew_share = total_stickers * 1/5

    # Calculate the number of stickers remaining after Andrew received his share
    remaining_stickers = total_stickers - andrew_share

    # Calculate the number of stickers Bill received
    bill_share = remaining_stickers * 3/10

    # Calculate the number of stickers Zander gave to both his friends
    zander_share = andrew_share + bill_share

    result = zander_share
    return result

print(solution())