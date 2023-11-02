def solution():
    """Annie has some money. The restaurant next door sells hamburgers for $4 each. The restaurant across the street sells milkshakes for $5 each. Annie buys 8 hamburgers and 6 milkshakes. She has $70 left. How much money, in dollars, did Annie have at first?"""
    # Define the cost of a hamburger and a milkshake
    HAMBURGER_PRICE = 4
    MILKSHAKE_PRICE = 5

    # Define the number of hamburgers and milkshakes purchased
    hamburgers_purchased = 8
    milkshakes_purchased = 6

    # Define the amount of money Annie has left
    money_left = 70

    # Calculate the total cost of the hamburgers and the milkshakes
    total_cost = (hamburgers_purchased * HAMBURGER_PRICE) + (milkshakes_purchased * MILKSHAKE_PRICE)

    # Calculate the amount of money Annie had at first
    money_at_first = total_cost + money_left

    # Display the amount of money Annie had at first
    result = money_at_first
    return result

print(solution())