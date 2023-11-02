def solution():
    # Find the total number of bids that were made on the desk
    total_bids = (65 - 15) / 5  # the price increased by $5 with each new bid
    # Divide the total number of bids by 2 to find how many times each person bid
    each_person_bid = total_bids / 2
    result = each_person_bid
    return result

print(solution())