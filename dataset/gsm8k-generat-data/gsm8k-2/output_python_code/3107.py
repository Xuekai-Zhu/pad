def solution():
    """Annie has $120. The restaurant next door sells hamburgers for $4 each. The restaurant across the street sells milkshakes for $3 each. Annie buys 8 hamburgers and 6 milkshakes. How much money, in dollars, does she have left?"""
    starting_money = 120
    hamburgers = 8
    hamburgers_price = 4
    milkshakes = 6
    milkshakes_price = 3
    total_spent = hamburgers * hamburgers_price + milkshakes * milkshakes_price
    remaining_money = starting_money - total_spent
    result = remaining_money
    return result

print(solution())