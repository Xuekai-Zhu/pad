def solution():
    
    starting_bid = 300
    harry_bid = starting_bid + 200
    second_bidder_bid = harry_bid * 2
    third_bidder_bid = second_bidder_bid + (harry_bid * 3)
    harry_final_bid = 4000
    difference = harry_final_bid - third_bidder_bid
    result = difference
    
    return result

print(solution())