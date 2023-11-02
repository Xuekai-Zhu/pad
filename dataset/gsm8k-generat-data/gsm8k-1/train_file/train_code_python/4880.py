def solution():
    """Snap, Crackle, and Pop spend $150 on cereal in a grocery store. Snap spends twice as much as Crackle. Crackle spends 3 times as much as Pop. How much did Pop spend?"""
    total_spent = 150
    crackle_spent = total_spent / (1 + 2 + 3)
    pop_spent = crackle_spent / 3
    result = pop_spent
    return result

print(solution())