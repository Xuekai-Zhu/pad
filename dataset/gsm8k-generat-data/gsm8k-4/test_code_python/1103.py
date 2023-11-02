def solution():
    """Martha is making centerpieces for her Thanksgiving dinner. 
    There are six centerpieces, and each centerpiece uses 8 roses, 
    twice as many orchids as roses, and a certain number of lilies. 
    If Martha wants to spend $2700 total, and each flower costs $15, 
    how many lilies will she put in each centerpiece?"""
    
    # Define the number of centerpieces
    NUM_CENTERPIECES = 6
    
    # Define the number of roses per centerpiece
    ROSES_PER_CENTERPIECE = 8
    
    # Define the number of orchids per centerpiece (twice as many as roses)
    ORCHIDS_PER_CENTERPIECE = ROSES_PER_CENTERPIECE * 2
    
    # Define the cost of each flower
    FLOWER_COST = 15
    
    # Calculate the total cost of all the flowers
    total_cost = NUM_CENTERPIECES * (ROSES_PER_CENTERPIECE + ORCHIDS_PER_CENTERPIECE + LILIES_PER_CENTERPIECE) * FLOWER_COST
    
    # Calculate the cost of the lilies in each centerpiece
    lily_cost_per_centerpiece = (total_cost - 2700) / (NUM_CENTERPIECES * LILIES_PER_CENTERPIECE)
    
    # Calculate the number of lilies that can be purchased per centerpiece with the remaining budget
    lilies_budget = lily_cost_per_centerpiece / FLOWER_COST
    
    result = round(lilies_budget)
    return result

print(solution())