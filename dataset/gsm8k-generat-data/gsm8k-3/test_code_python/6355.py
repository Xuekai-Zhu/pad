def solution():
    """Louis is making himself a velvet suit for a formal event. The velvet fabric he chose was $24 per yard. He bought a pattern for $15, and two spools of silver thread for $3 each. If he spent $141 for the pattern, thread, and fabric, how many yards of fabric did he buy?"""
    # Define the cost of the pattern and thread
    PATTERN_COST = 15
    THREAD_COST = 3 * 2

    # Define the cost per yard of velvet fabric
    VELVET_COST = 24

    # Define the total cost of the pattern, thread, and fabric
    TOTAL_COST = 141

    # Calculate the cost of the fabric
    fabric_cost = TOTAL_COST - PATTERN_COST - THREAD_COST

    # Calculate the number of yards of fabric Louis bought
    yards_bought = fabric_cost // VELVET_COST

    # Display the number of yards of fabric bought
    result = yards_bought
    return result

print(solution())