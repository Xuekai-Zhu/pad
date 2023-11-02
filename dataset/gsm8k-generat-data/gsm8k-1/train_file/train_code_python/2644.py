def solution():
    """Rebecca runs a hair salon. She charges $30 for haircuts, $40 for perms, and $60 for dye jobs, but she has to buy a box of hair dye for $10 to dye every head of hair. Today, she has four haircuts, one perm, and two dye jobs scheduled. If she makes $50 in tips, how much money will she have in dollars at the end of the day?"""
    haircut_price = 30
    perm_price = 40
    dye_price = 60
    dye_cost = 10
    num_haircuts = 4
    num_perms = 1
    num_dyes = 2
    
    # Calculate total revenue from haircuts, perms, and dyes
    total_revenue = (num_haircuts * haircut_price) + (num_perms * perm_price) + (num_dyes * (dye_price - dye_cost))
    
    # Add in tips
    total_revenue += 50
    
    result = total_revenue
    
    return result

print(solution())