def solution():
    # Calculate the cost of the clown
    cost_clown = 100 * 4  # The clown cost $100 per hour and was hired for 4 hours

    # Calculate the cost of the bounce house
    cost_bounce_house = (100 / 2) * 3 * 2  # The bounce house was rented for half the time, and cost 3 times more per hour than the clown

    # Calculate the cost of everything else
    cost_other = 1000

    # Calculate the total cost of the birthday party
    total_cost = cost_clown + cost_bounce_house + cost_other
    result = total_cost
    return result

print(solution())