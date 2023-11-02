def solution():
    total_amount = 50
    moses_share_percentage = 0.4

    # Calculate Moses' share
    moses_share = total_amount * moses_share_percentage

    # Calculate the remainder after Moses takes his share
    remainder = total_amount - moses_share

    # Calculate the amount Tony and Esther will each get from the remainder
    tony_and_esther_share = remainder / 2

    # Calculate the difference between Moses' share and Esther's share
    difference = moses_share - tony_and_esther_share

    result = difference
    return result

print(solution())