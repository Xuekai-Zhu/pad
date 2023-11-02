def solution():
    # Calculate Moses' share
    moses_share = 0.4 * 50

    # Calculate the remaining amount
    remaining_amount = 50 - moses_share

    # Calculate the amount each of Tony and Esther will get
    tony_esther_share = remaining_amount / 2

    # Calculate the difference between Moses' share and Esther's share
    difference = moses_share - tony_esther_share

    result = difference
    return result

print(solution())