def solution():
    zander_stickers = 100  # number of stickers Zander collected
    andrew_share = zander_stickers * (1/5)  # number of stickers Andrew received
    bill_share = (zander_stickers - andrew_share) * (3/10)  # number of stickers Bill received
    total_stickers_given = zander_stickers - andrew_share - bill_share  # total number of stickers given away by Zander
    stickers_given_by_andrew = total_stickers_given/2  # Andrew gave stickers to two friends, so he gave half of the total stickers
    result = stickers_given_by_andrew
    return result

print(solution())