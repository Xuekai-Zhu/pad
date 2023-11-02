def solution():
    total_stickers = 1500
    sas_ratio = 1 + 1 + 3  # Ratio of stickers shared among Susan, Andrew, and Sam
    sam_share = total_stickers * 3 / sas_ratio  # Number of stickers Sam received
    andrew_share = total_stickers * 1 / sas_ratio  # Number of stickers Andrew received
    susan_share = total_stickers * 1 / sas_ratio  # Number of stickers Susan received

    # Calculate how many stickers Andrew received from Sam
    stickers_from_sam = sam_share * (2 / 3)

    # Calculate Andrew's total number of stickers after receiving from Sam
    andrew_total = andrew_share + stickers_from_sam

    result = andrew_total
    return result

print(solution())