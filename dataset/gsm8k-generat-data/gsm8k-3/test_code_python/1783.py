def solution():
    """Mia has 4 times as many shells as David. Ava has 20 more shells than Mia. Alice has half the number of shells Ava has. If David has 15 shells, what the total number of conch shells they all have?"""
    # Define the number of shells David has
    david_shells = 15

    # Calculate the number of shells Mia has
    mia_shells = david_shells * 4

    # Calculate the number of shells Ava has
    ava_shells = mia_shells + 20

    # Calculate the number of shells Alice has
    alice_shells = ava_shells / 2

    # Calculate the total number of shells
    total_shells = david_shells + mia_shells + ava_shells + alice_shells

    # Display the total number of shells
    result = total_shells
    return result

print(solution())