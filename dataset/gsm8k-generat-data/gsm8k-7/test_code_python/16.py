def solution():
    johnson_share = 5
    mike_share = 2
    johnson_amount = 2500

    # Calculate the total share of both partners
    total_share = johnson_share + mike_share

    # Calculate the value of one share
    one_share_value = johnson_amount / johnson_share

    # Calculate Mike's share and subtract the cost of his shirt
    mike_amount = (mike_share * one_share_value) - 200
    result = mike_amount
    return result

print(solution())