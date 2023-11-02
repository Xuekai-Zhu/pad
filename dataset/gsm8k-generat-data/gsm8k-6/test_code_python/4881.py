def solution():
    # Calculate the amounts spent by Pop, Crackle, and Snap
    pop = x  # let x be the amount spent by Pop
    crackle = 3 * pop  # Crackle spends 3 times as much as Pop
    snap = 2 * crackle  # Snap spends twice as much as Crackle
    total = pop + crackle + snap  # total amount spent is $150

    # Solve for x
    x = (150 - 2 * crackle - snap) / 4
    result = x
    return result

print(solution())