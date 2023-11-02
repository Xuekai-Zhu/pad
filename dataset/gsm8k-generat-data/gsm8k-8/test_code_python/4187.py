def solution():
    # Calculate the initial amount of money Jeremy had
    initial_money = 2 * 3000

    # Calculate the cost of the accessories
    accessory_cost = 0.1 * 3000

    # Calculate the total cost of the purchase
    total_cost = 3000 + accessory_cost

    # Calculate how much money Jeremy has left after the purchase
    remaining_money = initial_money - total_cost
    result = remaining_money
    return result

print(solution())