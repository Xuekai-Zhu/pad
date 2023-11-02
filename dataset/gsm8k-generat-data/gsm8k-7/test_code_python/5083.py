def solution():
    starting_price = 15
    end_price = 65
    bid_increase = 5

    # Calculate the total number of bid increases
    num_increases = (end_price - starting_price) / bid_increase

    # Divide the number of increases evenly between the two people
    num_bids_per_person = num_increases / 2

    result = num_bids_per_person
    return result

print(solution())