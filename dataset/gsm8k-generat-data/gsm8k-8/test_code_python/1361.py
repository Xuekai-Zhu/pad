def solution():
    # Define the price of hamburgers and milkshakes
    hamburger_price = 4
    milkshake_price = 5

    # Define the number of hamburgers and milkshakes purchased
    num_hamburgers = 8
    num_milkshakes = 6

    # Calculate the total cost of the hamburgers and milkshakes
    total_cost = (num_hamburgers * hamburger_price) + (num_milkshakes * milkshake_price)

    # Calculate the initial amount of money Annie had
    initial_money = total_cost + 70
    result = initial_money
    return result

print(solution())