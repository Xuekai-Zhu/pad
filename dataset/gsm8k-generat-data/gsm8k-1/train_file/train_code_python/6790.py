def solution():
    """Mary bought a packet of 1500 stickers. She shared them between Susan, Andrew and Sam in the ratio 1:1:3 respectively. If Sam gave Andrew two-thirds of his own share, how many stickers does Andrew now have?"""
    total_stickers = 1500
    sas_ratio = 1 + 1 + 3 # ratio of Susan, Andrew and Sam
    sam_share = total_stickers * (3/5) # calculating Sam's share according to ratio
    andrew_share = (sam_share * 2)/3 # calculating Andrew's share after Sam gave him 2/3 of his own share
    result = andrew_share
    return result

print(solution())