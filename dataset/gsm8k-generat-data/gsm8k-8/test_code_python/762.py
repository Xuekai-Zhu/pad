def solution():
    # Calculate the total number of pens Lenny bought
    total_pens = 20 * 5

    # Calculate the number of pens Lenny gave to her friends
    pens_given_to_friends = 0.4 * total_pens

    # Calculate the number of pens left after giving some to friends
    pens_left = total_pens - pens_given_to_friends

    # Calculate the number of pens Lenny gave to her classmates
    pens_given_to_classmates = pens_left / 4

    # Calculate the number of pens left for Lenny
    pens_left_for_lenny = pens_left - pens_given_to_classmates

    result = pens_left_for_lenny
    return result

print(solution())