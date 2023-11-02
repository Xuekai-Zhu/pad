def solution():
    # Calculate the total number of parts in the ratio
    total_parts = 1 + 1 + 3

    # Calculate the size of one part
    one_part = 1500 / total_parts

    # Calculate the number of stickers Susan and Andrew each received
    susan_andrew = one_part * 2

    # Calculate the number of stickers Sam received
    sam = one_part * 3

    # Calculate the number of stickers Andrew received after Sam gave him two-thirds of his share
    andrew = susan_andrew + (2/3 * sam)

    result = andrew
    return result

print(solution())