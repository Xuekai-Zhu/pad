def solution():
    """Annie has $120. The restaurant next door sells hamburgers for $4 each. The restaurant across the street sells milkshakes for $3 each. Annie buys 8 hamburgers and 6 milkshakes. How much money, in dollars, does she have left?"""
    # Define the cost of a hamburger and a milkshake
    HAMBURGER_PRICE = 4
    MILKSHAKE_PRICE = 3

    # Define the number of hamburgers and milkshakes purchased
    hamburgers = 8
    milkshakes = 6

    # Calculate the cost of the hamburgers and milkshakes
    hamburger_cost = hamburgers * HAMBURGER_PRICE
    milkshake_cost = milkshakes * MILKSHAKE_PRICE

    # Calculate the total cost
    total_cost = hamburger_cost + milkshake_cost

    # Calculate the amount of money Annie has left
    remaining_money = 120 - total_cost

    # Display the remaining money
    result = remaining_money
    return result

print(solution())