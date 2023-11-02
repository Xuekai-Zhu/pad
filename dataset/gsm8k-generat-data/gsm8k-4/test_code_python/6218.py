def solution():
    """Blake bought 4 lollipops and 6 packs of chocolate. If each lollipop costs $2 and a pack of chocolate costs the same as four lollipops, how much change will Blake get back if he gave the cashier 6 $10 bills?"""
    # Define the cost of one lollipop and one pack of chocolate
    lollipop_cost = 2
    chocolate_pack_cost = lollipop_cost * 4

    # Calculate the total cost of the lollipops and the chocolate packs
    total_cost = (4 * lollipop_cost) + (6 * chocolate_pack_cost)

    # Calculate the amount paid by Blake
    amount_paid = 6 * 10

    # Calculate the change Blake will get back
    change = amount_paid - total_cost

    # return the result
    result = change
    return result

print(solution())