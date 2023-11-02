def solution():
    """The profit from a business transaction is shared among 2 business partners, Mike and Johnson in the ratio 2:5 respectively. If Johnson got $2500, how much will Mike have after spending some of his share on a shirt that costs $200?"""
    johnson_share = 5
    mike_share = 2
    total_share = johnson_share + mike_share
    johnson_amount = 2500
    mike_amount = (mike_share/total_share) * johnson_amount
    mike_amount -= 200  # Mike spent $200 on a shirt
    result = mike_amount
    return result

print(solution())