def solution():
    num_delegates = 36
    num_preprinted = 16

    # Calculate the number of delegates without pre-printed name badges
    num_remaining = num_delegates - num_preprinted

    # Calculate the number of delegates who made their own name badges
    num_handwritten = (num_remaining / 2)

    # Calculate the number of delegates not wearing name badges
    num_no_badges = num_delegates - num_preprinted - num_handwritten
    result = num_no_badges
    return result

print(solution())