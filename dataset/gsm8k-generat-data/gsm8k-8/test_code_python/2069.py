def solution():
    # Define Page's initial shoe collection
    initial_collection = 80

    # Calculate the number of shoes she donates
    donated_shoes = 0.30 * initial_collection

    # Calculate the number of shoes she has left after donating
    remaining_shoes = initial_collection - donated_shoes

    # Calculate the number of shoes she has after buying 6 more pairs
    new_collection = remaining_shoes + 6

    result = new_collection
    return result

print(solution())