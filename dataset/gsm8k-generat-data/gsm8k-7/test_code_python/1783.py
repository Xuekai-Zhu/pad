def solution():
    david_shells = 15
    mia_shells = 4 * david_shells
    ava_shells = mia_shells + 20
    alice_shells = ava_shells / 2

    # Calculate the total number of conch shells
    total_shells = david_shells + mia_shells + ava_shells + alice_shells
    result = total_shells
    return result

print(solution())