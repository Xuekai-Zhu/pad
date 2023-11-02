def solution():
    """Mary bought a packet of 1500 stickers. She shared them between Susan, Andrew and Sam in the ratio 1:1:3 respectively. If Sam gave Andrew two-thirds of his own share, how many stickers does Andrew now have?"""
    # Define the total number of stickers and the ratio of sharing
    TOTAL_STICKERS = 1500
    SHARE_RATIO = [1, 1, 3]

    # Calculate the number of stickers each person gets based on the sharing ratio
    total_shares = sum(SHARE_RATIO)
    susan_share = int((SHARE_RATIO[0] / total_shares) * TOTAL_STICKERS)
    andrew_share = int((SHARE_RATIO[1] / total_shares) * TOTAL_STICKERS)
    sam_share = int((SHARE_RATIO[2] / total_shares) * TOTAL_STICKERS)

    # Calculate the amount of stickers Sam gives Andrew
    andrew_received = int((2 / 3) * sam_share)
    sam_remaining = sam_share - andrew_received

    # Add the stickers to Andrew's share
    andrew_share += andrew_received

    # Display the number of stickers Andrew now has
    result = andrew_share
    return result

print(solution())