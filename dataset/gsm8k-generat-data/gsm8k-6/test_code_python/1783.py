def solution():
    # Find Mia's number of shells
    mia_shells = 4 * 15  # David has 15 shells

    # Find Ava's number of shells
    ava_shells = mia_shells + 20

    # Find Alice's number of shells
    alice_shells = ava_shells / 2

    # Calculate the total number of shells they all have
    total_shells = david_shells + mia_shells + ava_shells + alice_shells
    result = total_shells
    return result

print(solution())