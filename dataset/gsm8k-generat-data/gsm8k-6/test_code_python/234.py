def solution():
    # Calculate the total cost of Mark's purchase
    total_cost = 4.20 + 2.05

    # Calculate the amount of change Mark should receive
    change = 7.00 - total_cost

    # Calculate the number of nickels in Mark's change
    num_nickels = int((change - 0.25 - 0.10) / 0.05)

    result = num_nickels
    return result

print(solution())