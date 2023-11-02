def solution():
    
    starting_bid = 300
    harry_bid = starting_bid + 200
    second_bid = harry_bid * 2
    third_bid = second_bid + (3 * harry_bid)
    harry_final_bid = 4000
    difference = harry_final_bid - third_bid
    result = difference
    return result

print(solution())