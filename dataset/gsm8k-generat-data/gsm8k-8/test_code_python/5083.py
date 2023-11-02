def solution():
    # Define the starting price and final price
    starting_price = 15
    final_price = 65

    # Define the increment per bid
    increment = 5

    # Calculate the number of bids made by each person
    person1_bids = (final_price - starting_price) / (2 * increment)
    person2_bids = (final_price - starting_price) / (2 * increment)

    # Round up the number of bids to the nearest integer
    person1_bids = int(person1_bids + 0.5)
    person2_bids = int(person2_bids + 0.5)

    # Return the result as a tuple
    result = (person1_bids, person2_bids)
    return result

print(solution())