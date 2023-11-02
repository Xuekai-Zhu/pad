def solution():
    """Rebecca runs a hair salon. She charges $30 for haircuts, $40 for perms, and $60 for dye jobs, but she has to buy a box of hair dye for $10 to dye every head of hair. Today, she has four haircuts, one perm, and two dye jobs scheduled. If she makes $50 in tips, how much money will she have in dollars at the end of the day?"""
    # Define the prices and costs for each service
    HAIRCUT_PRICE = 30
    PERM_PRICE = 40
    DYE_PRICE = 60
    DYE_COST = 10

    # Define the number of each service scheduled
    haircuts = 4
    perms = 1
    dye_jobs = 2

    # Calculate the earnings from each service
    haircut_earnings = haircuts * HAIRCUT_PRICE
    perm_earnings = perms * PERM_PRICE
    dye_earnings = dye_jobs * DYE_PRICE
    dye_costs = dye_jobs * DYE_COST

    # Calculate the total earnings and tips
    total_earnings = haircut_earnings + perm_earnings + dye_earnings - dye_costs
    total_tips = 50

    # Calculate the final amount of money Rebecca has in dollars
    total_money = total_earnings + total_tips

    # Display the final amount of money
    result = total_money
    return result

print(solution())