def solution():
    # Number of shells David has
    david_shells = 15

    # Number of shells Mia has (4 times the number of shells David has)
    mia_shells = 4 * david_shells

    # Number of shells Ava has (20 more than the number of shells Mia has)
    ava_shells = mia_shells + 20

    # Number of shells Alice has (half the number of shells Ava has)
    alice_shells = ava_shells / 2

    # Total number of conch shells they all have
    total_shells = david_shells + mia_shells + ava_shells + alice_shells
    result = total_shells
    return result

print(solution())