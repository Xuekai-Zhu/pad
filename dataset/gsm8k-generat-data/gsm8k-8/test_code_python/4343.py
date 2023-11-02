def solution():
    # Calculate Janina's total daily expenses
    total_expenses = 30 + 12

    # Calculate the profit per pancake
    profit_per_pancake = 2 - (total_expenses / 100)

    # Calculate the number of pancakes Janina needs to sell to break even
    pancakes_needed = total_expenses / profit_per_pancake

    # Round up to the nearest whole number
    pancakes_needed = int(pancakes_needed + 0.5)

    result = pancakes_needed
    return result

print(solution())