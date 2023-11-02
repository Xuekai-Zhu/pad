def solution():
    total_stickers = 1500
    susan_share = total_stickers // 5  # 1/5 of total for Susan (1+1+3=5 parts in ratio)
    andrew_share = total_stickers // 5  # 1/5 of total for Andrew
    sam_share = total_stickers // 5 * 3  # 3/5 of total for Sam

    # Sam gives 2/3 of his share to Andrew
    sam_to_andrew = (2/3) * sam_share
    andrew_share += sam_to_andrew
    sam_share -= sam_to_andrew

    result = andrew_share
    return result

print(solution())