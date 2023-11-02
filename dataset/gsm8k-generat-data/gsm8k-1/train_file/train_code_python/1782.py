def solution():
    """Mia has 4 times as many shells as David. Ava has 20 more shells than Mia. Alice has half the number of shells Ava has. If David has 15 shells, what the total number of conch shells they all have?"""
    david_shells = 15
    mia_shells = david_shells * 4
    ava_shells = mia_shells + 20
    alice_shells = ava_shells / 2
    total_shells = david_shells + mia_shells + ava_shells + alice_shells
    result = total_shells
    return result

print(solution())