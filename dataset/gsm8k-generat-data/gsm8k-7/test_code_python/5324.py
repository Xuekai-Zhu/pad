def solution():
    parker_share = 2
    richie_share = 3
    parker_amount = 50

    # Find the ratio factor
    ratio_factor = parker_amount / parker_share

    # Calculate the total amount shared
    total_amount = (parker_share + richie_share) * ratio_factor
    result = total_amount
    return result

print(solution())