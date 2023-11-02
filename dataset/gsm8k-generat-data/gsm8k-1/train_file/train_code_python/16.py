def solution():
    """The profit from a business transaction is shared among 2 business partners, Mike and Johnson in the ratio 2:5 respectively. If Johnson got $2500, how much will Mike have after spending some of his share on a shirt that costs $200?"""
    johnson_share = 5
    mike_share = 2
    johnson_amount = 2500
    total_share = johnson_share + mike_share
    mike_amount = (mike_share / total_share) * (johnson_amount / (johnson_share / total_share))
    mike_amount -= 200  # subtract the cost of the shirt
    result = round(mike_amount, 2)
    return result

print(solution())