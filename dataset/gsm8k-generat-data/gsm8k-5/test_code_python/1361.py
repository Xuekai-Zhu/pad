def solution():
    hamburgers = 8  # Annie buys 8 hamburgers
    milkshakes = 6  # Annie buys 6 milkshakes
    hamburgers_cost = 4  # The cost of one hamburger is $4
    milkshakes_cost = 5  # The cost of one milkshake is $5

    # Calculate the total cost of hamburgers and milkshakes
    total_cost = (hamburgers * hamburgers_cost) + (milkshakes * milkshakes_cost)

    # Calculate the money Annie had at first
    initial_money = total_cost + 70
    result = initial_money
    return result

print(solution())