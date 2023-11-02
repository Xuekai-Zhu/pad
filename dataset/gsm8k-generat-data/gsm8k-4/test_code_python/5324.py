def solution():
    """Parker and Richie split a sum of money in the ratio 2:3. If Parker got $50 (which is the smaller share), how much did they share?"""
    # Define Parker's share and the ratio of the split
    parker_share = 50
    ratio = 2/3

    # Calculate the total share using Parker's share and the ratio
    total_share = parker_share / ratio

    # Calculate Parker's and Richie's share based on the ratio
    parker_share_ratio = (2 / 5) * total_share
    richie_share_ratio = (3 / 5) * total_share

    # Check if the calculated shares match the given information that Parker got $50
    if parker_share_ratio == parker_share:
        result = total_share
    else:
        result = "Invalid input"

    return result

print(solution())