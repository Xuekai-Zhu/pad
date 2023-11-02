def solution():
    """Carly is making a beaded corset. She's going to add 50 rows of purple beads with 20 beads per row, 40 rows of blue beads with 18 beads per row, and 80 gold beads. If beads cost $1 per 10 beads, how much do all the beads she bought cost?"""
    
    # Define the number of beads per row
    PURPLE_BEADS_PER_ROW = 20
    BLUE_BEADS_PER_ROW = 18
    
    # Define the cost per 10 beads
    BEAD_COST = 1 
    
    # Calculate the total number of purple beads
    purple_beads = 50 * PURPLE_BEADS_PER_ROW
    
    # Calculate the total number of blue beads
    blue_beads = 40 * BLUE_BEADS_PER_ROW
    
    # Calculate the total number of gold beads
    gold_beads = 80
    
    # Calculate the total number of beads
    total_beads = purple_beads + blue_beads + gold_beads
    
    # Calculate the total cost of the beads
    total_cost = total_beads / 10 * BEAD_COST
    
    # Display the total cost
    result = total_cost
    return result

print(solution())