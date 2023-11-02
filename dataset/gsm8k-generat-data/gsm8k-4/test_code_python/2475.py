def solution():
    """Sarah bought 12 lollipops filled with caramel for a total of 3 dollars. She offered to share one-quarter of the lollipops with her friend, Julie, but Julie insisted on reimbursing Sarah for the cost of the lollipops shared. How much money, in cents, did Julie give Sarah to pay for the shared lollipops?"""
    # Define the number of lollipops and the total cost
    num_lollipops = 12
    total_cost = 3

    # Calculate the cost per lollipop
    cost_per_lollipop = total_cost / num_lollipops

    # Calculate the number of lollipops shared with Julie
    num_shared = num_lollipops / 4

    # Calculate the cost of the shared lollipops
    shared_cost = num_shared * cost_per_lollipop

    # Convert the shared cost to cents and return the result
    result = int(shared_cost * 100)
    return result

print(solution())