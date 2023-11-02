def solution():
    amy_share = 50
    amy_ratio = 1
    sandra_ratio = 2
    ruth_ratio = 3

    # Calculate the total ratio of the three cousins
    total_ratio = amy_ratio + sandra_ratio + ruth_ratio

    # Calculate the ratio of Sandra's share
    sandra_share_ratio = (amy_share / amy_ratio) * sandra_ratio

    # Calculate the total amount of money shared
    total_amount = sandra_share_ratio + amy_share + (ruth_ratio / total_ratio)

    # Calculate the amount Sandra got
    sandra_share = (sandra_share_ratio / total_amount) * total_amount
    result = sandra_share
    return result

print(solution())