def solution():
    # Calculate the total cost of the meal
    total_cost = (40 + 15 + 25) * 1.1  # add 10% service charge
    total_cost *= 1.05  # add 5% tip

    # Calculate the change Mr. Arevalo will receive from his $100
    change = 100 - total_cost
    result = change
    return result

print(solution())