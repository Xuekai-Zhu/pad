def solution():
    # Calculate the number of stickers each person gets
    total_part = 1+1+3  # total parts in the ratio
    susan_share = (1/total_part) * 1500
    andrew_share = (1/total_part) * 1500
    sam_share = (3/total_part) * 1500

    # Calculate how many stickers Andrew gets after Sam gives him two-thirds of his share
    sam_gives_andrew = (2/3) * sam_share
    andrew_has = andrew_share + sam_gives_andrew
    result = andrew_has
    return result

print(solution())