def solution():
    # Calculate the cost of the clown
    cost_clown = 100 * 4  # the clown cost $100 per hour for 4 hours

    # Calculate the cost of the bounce house
    cost_bounce_house = (100 * 3) * 2  # the bounce house cost 3 times as much per hour and was rented for half the time of the clown

    # Calculate the total cost of the party
    total_cost = cost_clown + cost_bounce_house + 1000  # add the cost of the clown, bounce house, and other party expenses

    result = total_cost
    return result

print(solution())