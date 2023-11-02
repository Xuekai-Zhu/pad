def solution():
    """Annie has $120. The restaurant next door sells hamburgers for $4 each. The restaurant across the street sells milkshakes for $3 each. Annie buys 8 hamburgers and 6 milkshakes. How much money, in dollars, does she have left?"""
    # Define the initial amount of money
    initial_money = 120

    # Define the price of a hamburger and the number of hamburgers purchased
    hamburger_price = 4
    hamburgers = 8

    # Define the price of a milkshake and the number of milkshakes purchased
    milkshake_price = 3
    milkshakes = 6

    # Calculate the total cost of the purchase
    total_cost = (hamburger_price * hamburgers) + (milkshake_price * milkshakes)

    # Calculate the amount of money left
    money_left = initial_money - total_cost

    # Return the result
    result = money_left
    return result

print(solution())