def solution():
    num_boxes = 20
    pens_per_box = 5
    total_pens = num_boxes * pens_per_box

    # Calculate the number of pens given to close friends
    pens_given_to_friends = 0.4 * total_pens

    # Calculate the number of pens left
    pens_left = total_pens - pens_given_to_friends

    # Calculate the number of pens given to classmates
    pens_given_to_classmates = 0.25 * pens_left

    # Calculate the final number of pens left
    pens_left = pens_left - pens_given_to_classmates
    result = pens_left
    return result

print(solution())