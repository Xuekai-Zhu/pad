def solution():
    starting_bid = 300  # the auction starts at $300
    harry_bid = starting_bid + 200  # Harry's first bid is $200 more than the starting bid
    second_bid = harry_bid * 2  # the second bidder doubles the bid
    third_bidder_added = 3 * harry_bid  # the third bidder adds three times Harry's bid
    final_harry_bid = 4000  # Harry's final bid is $4,000

    # Calculate how much Harry's final bid exceeds that of the third bidder
    excess = final_harry_bid - third_bidder_added
    result = excess
    return result

print(solution())