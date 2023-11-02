def solution():
    hamburgers = 8  # number of hamburgers purchased
    milkshakes = 6  # number of milkshakes purchased
    hamburgers_cost = 4  # cost of one hamburger
    milkshakes_cost = 5  # cost of one milkshake
    remaining_money = 70  # money left after purchasing

    # Calculate the total cost of hamburgers and milkshakes
    total_cost = (hamburgers * hamburgers_cost) + (milkshakes * milkshakes_cost)

    # Calculate the initial amount of money Annie had
    initial_money = total_cost + remaining_money
    result = initial_money
    return result

print(solution())