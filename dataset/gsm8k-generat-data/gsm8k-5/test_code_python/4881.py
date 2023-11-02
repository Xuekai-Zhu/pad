def solution():
    total_spent = 150  # Snap, Crackle, and Pop spend $150 on cereal
    pop_spent = total_spent / 10  # Let's assume Pop spent 1/10th of the total amount

    crackle_spent = 3 * pop_spent  # Crackle spent 3 times as much as Pop
    snap_spent = 2 * crackle_spent  # Snap spent twice as much as Crackle

    # Check if the total amount spent is correct
    if snap_spent + crackle_spent + pop_spent == total_spent:
        result = pop_spent
    else:
        result = "Error: incorrect total amount spent"
    return result

print(solution())