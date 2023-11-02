def solution():
    # Define the ratio of Sandra's share to Amy's share
    sandra_to_amy_ratio = 2/1

    # Define the ratio of Ruth's share to Amy's share
    ruth_to_amy_ratio = 3/1

    # Calculate the total amount of money shared
    total_amount = 50 / (1/ sandra_to_amy_ratio + 1 + 1/ ruth_to_amy_ratio)

    # Calculate the amount Sandra got
    sandra_share = sandra_to_amy_ratio * (total_amount / (sandra_to_amy_ratio + 1 + ruth_to_amy_ratio))

    result = sandra_share
    return result

print(solution())