def solution():
    """Caitlin makes bracelets to sell at the farmer’s market every weekend. Each bracelet takes twice as many small beads as it does large beads. If each bracelet uses 12 large beads, and Caitlin has 528 beads with equal amounts of large and small beads, how many bracelets can she make for this weekend?"""
    
    # Define the number of large beads needed per bracelet
    LARGE_BEADS_PER_BRACELET = 12
    
    # Calculate the total number of large beads Caitlin has
    total_large_beads = 528 / 2
    
    # Calculate the number of bracelets Caitlin can make
    small_beads_per_bracelet = 2 * LARGE_BEADS_PER_BRACELET
    num_bracelets = total_large_beads / LARGE_BEADS_PER_BRACELET
    
    # Display the number of bracelets Caitlin can make
    result = num_bracelets
    return result

print(solution())