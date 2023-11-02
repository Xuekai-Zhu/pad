def solution():
    """The novelty shop on the Starship Conundrum sells magazines and chocolates.  The cost of four chocolate bars is equal to the cost of 8 magazines.  If one magazine costs $1, how much does a dozen chocolate bars cost, in dollars?"""
    # Define the cost of one magazine and use it to calculate the cost of 8 magazines
    magazine_cost = 1
    magazine_quantity = 8
    magazine_total = magazine_cost * magazine_quantity

    # Use the relationship between chocolate and magazine costs to calculate the cost of 4 chocolate bars
    chocolate_total = magazine_total

    # Use the cost of 4 chocolate bars to calculate the cost of one chocolate bar
    chocolate_cost = chocolate_total / 4

    # Use the cost of one chocolate bar to calculate the cost of a dozen chocolate bars
    chocolate_quantity = 12
    total_cost = chocolate_cost * chocolate_quantity

    # Display the total cost of a dozen chocolate bars
    result = total_cost
    return result

print(solution())