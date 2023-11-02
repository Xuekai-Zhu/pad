def solution():
    """Debby and Maggie agreed to share a sum of money so that Debby takes 25% and Maggie takes the rest. If Maggie's share is $4,500, how much did they share?"""
    maggie_share = 4500
    debby_share = maggie_share / 0.75
    total_share = maggie_share + debby_share
    result = total_share
    return result

print(solution())