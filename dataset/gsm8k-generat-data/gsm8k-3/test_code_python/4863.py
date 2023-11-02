def solution():
    """Harry participates in the auction of a classic painting. The auction starts at $300, Harry is the first to bid, adding $200 to the starting value, a second bidder doubles the bid, and a third bidder adds three times Harry's bid. Finally, Harry bids $4,000. By how much did Harry's final bid exceed that of the third bidder?"""
    # Define the starting bid and Harry's bid increments
    START_BID = 300
    HARRY_INC = 200

    # Calculate the second bidder's bid
    second_bid = START_BID * 2

    # Calculate Harry's third bid increment
    harry_third_inc = HARRY_INC * 3

    # Calculate the third bidder's bid
    third_bid = START_BID + HARRY_INC + second_bid + harry_third_inc

    # Calculate the difference between Harry's final bid and the third bidder's bid
    diff = 4000 - third_bid

    # Display the difference
    result = diff
    return result

print(solution())