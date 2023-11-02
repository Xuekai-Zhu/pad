def solution():
    """Sarah bought 12 lollipops filled with caramel for a total of 3 dollars. She offered to share one-quarter of the lollipops with her friend,
    Julie, but Julie insisted on reimbursing Sarah for the cost of the lollipops shared. How much money, in cents, did Julie give Sarah to pay for the shared lollipops?"""
    total_lollipops = 12
    total_cost = 300  # in cents
    shared_lollipops = total_lollipops // 4
    shared_cost = total_cost // 4
    result = shared_cost
    return result

print(solution())