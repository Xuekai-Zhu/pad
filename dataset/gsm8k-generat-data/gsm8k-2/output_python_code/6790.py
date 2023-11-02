def solution():
    """Mary bought a packet of 1500 stickers. She shared them between Susan, Andrew and Sam in the ratio 1:1:3 respectively. If Sam gave Andrew two-thirds of his own share, how many stickers does Andrew now have?"""
    total_stickers = 1500
    sam_share = total_stickers * 3 / 5
    andrew_share = total_stickers / 5
    andrew_new_share = andrew_share + (2 / 3 * (sam_share / 3))
    result = andrew_new_share
    return result

print(solution())