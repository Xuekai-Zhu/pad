def solution():
    # Calculate the total cost of the board games
    total_cost = 6 * 15

    # Calculate the amount of change Jed received
    change = 100 - total_cost

    # Calculate the number of $5 bills Jed received
    num_bills = change // 5

    result = num_bills
    return result

print(solution())