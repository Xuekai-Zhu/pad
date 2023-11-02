def solution():
    total_money = 50  # Total amount to be shared by Tony, Moses and Esther
    moses_share = 0.4 * total_money  # Moses takes 40% of the total amount
    remainder = total_money - moses_share  # Tony and Esther split the remainder equally
    tony_share = remainder / 2  # Tony's share
    esther_share = remainder / 2  # Esther's share

    # Calculate how much more than Esther Moses will get
    more_than_esther = moses_share - esther_share
    result = more_than_esther
    return result

print(solution())