def solution():
    """James gets 3 parking tickets.  The first 2 cost $150 each and the third cost 1/3 as much as one of these.  His roommate agrees to pay half the cost.  How much money does he have left if he had $500 in the bank?"""
    # Define the cost of the first two parking tickets
    first_two_cost = 150 * 2

    # Define the cost of the third parking ticket
    third_cost = first_two_cost / 3

    # Calculate the total cost of the parking tickets
    total_cost = first_two_cost + third_cost

    # Calculate James' share of the cost
    james_share = total_cost / 2

    # Calculate how much money James has left after paying for the parking tickets
    money_left = 500 - james_share

    result = money_left
    return result

print(solution())