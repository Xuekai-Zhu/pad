def solution():
    # Calculate the total cost of the 6 board games
    total_cost = 6 * 15

    # Calculate the amount of change Jed should receive
    change = 100 - total_cost

    # Calculate the number of $5 bills in the change
    num_fives = change // 5

    result = num_fives
    return result

print(solution())