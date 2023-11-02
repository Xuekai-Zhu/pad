def solution():
    """Annie has some money. The restaurant next door sells hamburgers for $4 each. The restaurant across the street sells milkshakes for $5 each. Annie buys 8 hamburgers and 6 milkshakes. She has $70 left. How much money, in dollars, did Annie have at first?"""
    hamburgers_cost = 4
    milkshakes_cost = 5
    hamburgers_bought = 8
    milkshakes_bought = 6
    total_spent = (hamburgers_cost * hamburgers_bought) + (milkshakes_cost * milkshakes_bought)
    initial_money = total_spent + 70
    result = initial_money
    return result

print(solution())