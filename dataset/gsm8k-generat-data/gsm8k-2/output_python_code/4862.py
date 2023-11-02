def solution():
    """Harry participates in the auction of a classic painting. The auction starts at $300, Harry is the first to bid, adding $200 to the starting value, a second bidder doubles the bid, and a third bidder adds three times Harry's bid. Finally, Harry bids $4,000. By how much did Harry's final bid exceed that of the third bidder?"""
    starting_bid = 300
    harry_bid = starting_bid + 200
    second_bid = harry_bid * 2
    third_bid = second_bid + (3 * harry_bid)
    harry_final_bid = 4000
    difference = harry_final_bid - third_bid
    result = difference
    return result

print(solution())