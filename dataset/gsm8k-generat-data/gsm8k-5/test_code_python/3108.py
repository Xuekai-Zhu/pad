def solution():
    starting_money = 120  # Annie starts with $120
    hamburgers_bought = 8  # Annie buys 8 hamburgers
    milkshakes_bought = 6  # Annie buys 6 milkshakes
    cost_of_hamburgers = hamburgers_bought * 4  # Each hamburger costs $4
    cost_of_milkshakes = milkshakes_bought * 3  # Each milkshake costs $3
    total_cost = cost_of_hamburgers + cost_of_milkshakes  # Calculate the total cost of the purchase
    money_left = starting_money - total_cost  # Calculate how much money Annie has left
    result = money_left
    return result

print(solution())