def solution():
    # Calculate the total number of pens
    total_pens = 20 * 5  # 20 boxes with 5 pens each

    # Calculate the number of pens given to friends
    pens_given_to_friends = int(0.4 * total_pens)

    # Calculate the number of pens left after giving to friends
    pens_left = total_pens - pens_given_to_friends

    # Calculate the number of pens given to classmates
    pens_given_to_classmates = int(pens_left / 4)

    # Calculate the number of pens left after giving to classmates
    pens_remaining = pens_left - pens_given_to_classmates

    result = pens_remaining
    return result

print(solution())