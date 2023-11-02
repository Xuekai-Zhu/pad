def solution():
    man_share = 1/2  # fraction of the lot owned by the man
    sold_share = 1/10 * man_share  # fraction of man's share sold
    sold_share_value = 460  # value of the sold share
    # find the value of the entire lot using proportion
    man_share_value = sold_share_value / sold_share
    lot_value = man_share_value / man_share
    result = lot_value
    return result

print(solution())