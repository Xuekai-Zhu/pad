def solution():
    # Define the prices of the items and calculate the total cost before discounts
    milk_cost = 4.00 / 2
    bread_cost = 3.50
    detergent_cost = 10.25 - 1.25
    bananas_cost = 2 * 0.75
    total_cost = milk_cost + bread_cost + detergent_cost + bananas_cost

    # Calculate Josie's change after paying with the $20 bill
    change = 20 - total_cost
    result = change
    return result

print(solution())