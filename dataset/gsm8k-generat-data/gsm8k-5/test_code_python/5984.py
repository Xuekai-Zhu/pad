def solution():
    maggie_share = 4500  # Maggie's share is $4,500
    debby_share_fraction = 0.25  # Debby takes 25%

    # Calculate the total share
    total_share = maggie_share / (1 - debby_share_fraction)

    result = total_share
    return result

print(solution())