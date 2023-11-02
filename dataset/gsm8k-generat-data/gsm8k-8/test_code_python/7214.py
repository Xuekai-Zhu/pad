def solution():
    # Calculate the total cost of the items purchased
    total_cost = 2.75 + 1.5 + 11.5

    # Calculate the remaining amount of money after the purchases
    remaining_money = 40 - total_cost

    # Convert the remaining money to quarters
    quarters = remaining_money // 0.25

    result = quarters
    return result

print(solution())