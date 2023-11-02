def solution():
    """Rebecca runs a hair salon. She charges $30 for haircuts, $40 for perms, and $60 for dye jobs, but she has to buy a box of hair dye for $10 to dye every head of hair. Today, she has four haircuts, one perm, and two dye jobs scheduled. If she makes $50 in tips, how much money will she have in dollars at the end of the day?"""
    # Define the prices for each service and the cost of hair dye
    haircut_price = 30
    perm_price = 40
    dye_price = 60
    dye_cost = 10

    # Calculate the total revenue from haircuts
    haircut_revenue = 4 * haircut_price

    # Calculate the total revenue from perms
    perm_revenue = 1 * perm_price

    # Calculate the total revenue from dye jobs
    dye_revenue = 2 * dye_price - 2 * dye_cost

    # Calculate the total revenue including tips
    total_revenue = haircut_revenue + perm_revenue + dye_revenue + 50

    # Format the result as a dollar amount
    result = "${:,.2f}".format(total_revenue)
    return result

print(solution())