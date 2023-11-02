def solution():
    total_cost = 4.20 + 2.05  # Mark buys bread and cheese
    amount_paid = 7.00  # Mark gives the cashier $7.00
    change = amount_paid - total_cost  # Calculate the change Mark gets back

    # Calculate the number of nickels in the change
    num_nickels = int((change - 0.35) / 0.05)

    result = num_nickels
    return result

print(solution())