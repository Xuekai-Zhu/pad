def solution():
    """Mary bought a packet of 1500 stickers. She shared them between Susan, Andrew and Sam in the ratio 1:1:3 respectively. If Sam gave Andrew two-thirds of his own share, how many stickers does Andrew now have?"""
    # Define the total number of stickers and the sharing ratio
    total_stickers = 1500
    ratio = [1, 1, 3]

    # Calculate the total number of parts in the ratio
    total_ratio_parts = sum(ratio)

    # Calculate the size of one part in the ratio
    one_part = total_stickers / total_ratio_parts

    # Calculate the number of stickers received by each person
    susan_stickers = one_part * ratio[0]
    andrew_stickers = one_part * ratio[1]
    sam_stickers = one_part * ratio[2]

    # Calculate the number of stickers given by Sam to Andrew
    sam_to_andrew = (2/3) * sam_stickers

    # Add the stickers given by Sam to Andrew
    andrew_stickers += sam_to_andrew

    result = andrew_stickers
    return result

print(solution())