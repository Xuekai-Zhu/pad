def solution():
    """The profit from a business transaction is shared among 2 business partners, Mike and Johnson in the ratio 2:5 respectively. If Johnson got $2500, how much will Mike have after spending some of his share on a shirt that costs $200?"""
    # Define the ratio between Mike and Johnson's share
    mike_share = 2
    johnson_share = 5

    # Calculate the total share
    total_share = mike_share + johnson_share

    # Calculate Johnson's share
    johnson_amount = 2500

    # Calculate the ratio multiplier
    ratio_multiplier = johnson_amount / (johnson_share)

    # Calculate Mike's share
    mike_amount = ratio_multiplier * (mike_share)

    # Subtract the cost of the shirt from Mike's share
    mike_amount -= 200

    result = mike_amount
    return result

print(solution())