def solution():
    # Calculate the bids of the second and third bidder
    second_bidder = 2 * 500  # double the bid of Harry
    third_bidder = 3 * 200 + 500  # three times Harry's initial bid plus second bidder's bid

    # Calculate how much Harry's final bid exceeded that of the third bidder
    diff = 4000 - third_bidder
    result = diff
    return result

print(solution())