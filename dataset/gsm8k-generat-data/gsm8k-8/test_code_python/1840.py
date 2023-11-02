def solution():
    # Convert 95 cents to number of nickels
    num_nickels = 95 // 5

    # Subtract 1 nickel for the 25 cents Ray gives to Peter
    num_nickels -= 1

    # Calculate how much Ray gives to Randi
    randi_cents = 2 * 25

    # Convert Randi's amount to number of nickels and subtract from original number of nickels
    num_nickels -= randi_cents // 5

    result = num_nickels
    return result

print(solution())