def solution():
    """The novelty shop on the Starship Conundrum sells magazines and chocolates. The cost of four chocolate bars is equal to the cost of 8 magazines. If one magazine costs $1, how much does a dozen chocolate bars cost, in dollars?"""
    
    # Define the cost of one magazine
    magazine_cost = 1
    
    # Calculate the cost of one chocolate bar
    chocolate_cost = (8 * magazine_cost) / 4
    
    # Calculate the cost of a dozen chocolate bars
    dozen_chocolate_cost = 12 * chocolate_cost
    
    result = dozen_chocolate_cost
    return result

print(solution())