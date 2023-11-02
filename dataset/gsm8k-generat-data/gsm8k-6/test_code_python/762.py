def solution():
    # Calculate the total number of pens Lenny bought
    total_pens = 20 * 5

    # Calculate the number of pens Lenny gave to her friends
    pens_to_friends = 0.4 * total_pens

    # Calculate the number of pens Lenny has left
    pens_left = total_pens - pens_to_friends

    # Calculate the number of pens Lenny gave to her classmates
    pens_to_classmates = pens_left / 4

    # Calculate the number of pens Lenny has left after giving some to her classmates
    pens_left = pens_left - pens_to_classmates

    result = pens_left
    return result

print(solution())