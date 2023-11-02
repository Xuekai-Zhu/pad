def solution():
    # Calculate the cost of the hamburger meat
    hamburger_cost = 2 * 3.5  # 2 pounds of hamburger meat at $3.50 per pound

    # Calculate the total cost of the groceries
    total_cost = hamburger_cost + 1.5 + 1 + (2 * 1.5) + 2.5 - 1  # Hamburger buns, lettuce, tomato, pickles (-$1 coupon)

    # Calculate the change Lauren would get back if she paid with a $20 bill
    change = 20 - total_cost
    result = change
    return result

print(solution())