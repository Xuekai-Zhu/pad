def solution():
    starting_price = 15  # The desk starts at $15
    final_price = 65  # The desk sells for $65
    increment = 5  # The price increases by $5 every time someone new bids
    num_bids = (final_price - starting_price) / increment  # Calculate the total number of bids
    person1_bids = (num_bids + 1) / 2  # Each person makes an equal number of bids
    person2_bids = num_bids - person1_bids  # Calculate how many bids the other person made
    result = (person1_bids, person2_bids)  # Return a tuple of the bids made by each person
    return result

print(solution())