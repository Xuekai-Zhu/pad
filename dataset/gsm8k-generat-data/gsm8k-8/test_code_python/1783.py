def solution():
    # Calculate Mia's number of shells
    mia_shells = 4 * 15

    # Add 20 to Mia's shells to get Ava's shells
    ava_shells = mia_shells + 20

    # Divide Ava's shells by 2 to get Alice's shells
    alice_shells = ava_shells / 2

    # Calculate the total number of shells
    total_shells = david_shells + mia_shells + ava_shells + alice_shells
    result = total_shells
    return result

print(solution())