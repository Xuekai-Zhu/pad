def solution():
    """Parker and Richie split a sum of money in the ratio 2:3. If Parker got $50 (which is the smaller share), how much did they share?"""
    parker_share = 2
    richie_share = 3
    total_share = parker_share + richie_share
    parker_amount = 50
    total_amount = parker_amount * total_share / parker_share
    result = total_amount
    return result

print(solution())