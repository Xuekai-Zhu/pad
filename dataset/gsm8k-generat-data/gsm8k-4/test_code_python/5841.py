def solution():
    """Tony, Moses and Esther are to share $50. Moses will take 40% of the total amount while Tony and Esther will split the remainder equally among themselves. How much more than Esther will Moses get?"""
    # Define the total amount to be shared
    total_amount = 50

    # Calculate the amount Moses will take
    moses_amount = total_amount * 0.4

    # Calculate the remaining amount to be split between Tony and Esther
    remaining_amount = total_amount - moses_amount

    # Calculate the amount each of Tony and Esther will get
    tony_esther_amount = remaining_amount / 2

    # Calculate how much more Moses will get than Esther
    difference = moses_amount - tony_esther_amount

    result = difference
    return result

print(solution())