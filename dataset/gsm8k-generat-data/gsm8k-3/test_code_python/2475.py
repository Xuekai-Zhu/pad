def solution():
    """Sarah bought 12 lollipops filled with caramel for a total of 3 dollars.  She offered to share one-quarter of the lollipops with her friend, Julie, but Julie insisted on reimbursing Sarah for the cost of the lollipops shared.  How much money, in cents, did Julie give Sarah to pay for the shared lollipops?"""
    # Calculate the cost of one lollipop
    cost_per_lollipop = 3 / 12

    # Calculate the number of lollipops Sarah will share with Julie
    num_shared_lollipops = 12 / 4

    # Calculate the cost of the lollipops Sarah will share with Julie
    shared_lollipop_cost = num_shared_lollipops * cost_per_lollipop

    # Convert the shared lollipop cost to cents
    shared_lollipop_cost_cents = shared_lollipop_cost * 100

    # Round the shared lollipop cost to the nearest cent
    shared_lollipop_cost_cents = round(shared_lollipop_cost_cents)

    # Display the amount Julie gave to Sarah
    result = shared_lollipop_cost_cents
    return result

print(solution())