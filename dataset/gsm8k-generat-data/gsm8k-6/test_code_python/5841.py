def solution():
    total_amount = 50  # total amount to be shared
    moses_share = 0.4 * total_amount  # Moses takes 40% of the total amount
    remaining_amount = total_amount - moses_share  # remaining amount after Moses takes his share
    tony_esther_share = remaining_amount / 2  # Tony and Esther split the remainder equally
    difference = moses_share - tony_esther_share  # difference between Moses' share and Esther's share
    result = difference
    return result

print(solution())