def solution():
    """Parker and Richie split a sum of money in the ratio 2:3. If Parker got $50 (which is the smaller share), how much did they share?"""
    # Calculate the ratio between Parker's share and Richie's share
    parker_share = 2
    richie_share = 3

    # Calculate the total amount of money they shared
    total_share = parker_share + richie_share

    # Calculate how much they shared in total, given that Parker got $50
    total_amount = 50 * total_share / parker_share

    # Display how much they shared in total
    result = total_amount
    return result

print(solution())