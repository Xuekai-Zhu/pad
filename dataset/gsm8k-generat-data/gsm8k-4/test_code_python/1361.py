def solution():
    """Annie has some money. The restaurant next door sells hamburgers for $4 each.
    The restaurant across the street sells milkshakes for $5 each. Annie buys 8 hamburgers and 6 milkshakes.
    She has $70 left. How much money, in dollars, did Annie have at first?"""
    # Define the prices of hamburgers and milkshakes
    HAMBURGER_PRICE = 4
    MILKSHAKE_PRICE = 5

    # Define the number of hamburgers and milkshakes Annie bought
    hamburgers = 8
    milkshakes = 6

    # Define the amount of money Annie has left after buying the hamburgers and milkshakes
    left_money = 70

    # Calculate the total cost of the hamburgers and milkshakes
    total_cost = (hamburgers * HAMBURGER_PRICE) + (milkshakes * MILKSHAKE_PRICE)

    # Calculate how much money Annie had at first
    initial_money = total_cost + left_money

    result = initial_money
    return result

print(solution())