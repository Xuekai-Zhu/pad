def solution():
    """Harry participates in the auction of a classic painting. The auction starts at $300, Harry is the first to bid, adding $200 to the starting value, a second bidder doubles the bid, and a third bidder adds three times Harry's bid. Finally, Harry bids $4,000. By how much did Harry's final bid exceed that of the third bidder?"""
    # Define the starting bid price and Harry's bid increment
    starting_bid = 300
    harry_bid_increment = 200

    # Calculate the second bidder's bid
    second_bid = starting_bid * 2

    # Calculate Harry's third bid
    third_bid = starting_bid + harry_bid_increment + second_bid + (harry_bid_increment * 3)

    # Calculate the difference between Harry's final bid and the third bidder's bid
    final_bid = 4000
    third_bidder_bid = third_bid
    difference = final_bid - third_bidder_bid

    # return the result
    result = difference
    return result

print(solution())