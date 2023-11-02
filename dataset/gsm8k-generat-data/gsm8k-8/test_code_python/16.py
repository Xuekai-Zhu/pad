def solution():
    # Define the ratio of Mike's share to Johnson's share
    mike_to_johnson_ratio = 2/5

    # Calculate the total profit
    johnson_share = 2500
    total_share = johnson_share / mike_to_johnson_ratio

    # Calculate Mike's share
    mike_share = total_share - johnson_share

    # Calculate Mike's share after spending $200 on a shirt
    mike_share_after_shirt = mike_share - 200

    result = mike_share_after_shirt
    return result

print(solution())