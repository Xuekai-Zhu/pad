def solution():
    """Sam shared a sum of money between his three cousins Sandra, Amy and Ruth in the ratio 2:1:3 respectively. If Amy got $50, how much did Sandra get?"""
    amy_share = 1
    sandra_share = 2
    ruth_share = 3
    amy_amount = 50
    total_shares = amy_share + sandra_share + ruth_share
    sandra_amount = (sandra_share / total_shares) * (amy_amount / amy_share) * sandra_share
    result = sandra_amount
    return result

print(solution())