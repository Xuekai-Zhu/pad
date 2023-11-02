def solution():
    """Gary is buying chlorine for his rectangular pool, which is 10 feet long, 8 feet wide, and 6 feet deep. Gary needs to buy one quart of chlorine for every 120 cubic feet of water in his pool. If chlorine costs $3 a quart, how much does Gary spend on chlorine?"""
    
    # Calculate the volume of water in the pool
    volume = 10 * 8 * 6
    
    # Calculate the number of quarts of chlorine needed
    chlorine = volume / 120
    
    # Calculate the total cost of the chlorine
    cost = chlorine * 3
    
    # Display the cost
    result = cost
    return result

print(solution())