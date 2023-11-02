def solution():
    # Set starting bid and increment
    starting_bid = 300
    increment = 200

    # Calculate second and third bidder's bids
    second_bid = 2 * (starting_bid + increment)
    third_bid = starting_bid + increment + 3 * increment

    # Calculate difference between Harry's final bid and third bidder's bid
    difference = 4000 - third_bid
    result = difference
    return result

print(solution())