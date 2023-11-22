def solution():
    
    # Define the initial cost of the desk
    initial_cost = 200

    # Define the number of bids rised by each person
    bid_per_person = 1

    # Define the number of other people who bid once
    num_other_people = 3

    # Calculate the total number of bids rised
    total_bid_rise = bid_per_person * num_other_people

    # Calculate the total cost of the desk
    total_cost = initial_cost + total_bid_rise

    # Display the total cost
    result = total_cost
    return result

print(solution())