def solution():
    """Ronald is rolling a die and won't stop rolling until the average of all his rolls is a 3. He rolls a 1, a 3, a 2, a 4, a 3, a 5, a 3, a 4, a 4 and a 2. What does he need to roll on the next roll to be able to stop?"""
    # Define the list of previous rolls
    rolls = [1, 3, 2, 4, 3, 5, 3, 4, 4, 2]

    # Calculate the current average of the rolls
    current_avg = sum(rolls) / len(rolls)

    # Calculate the next roll needed to reach an average of 3
    # Formula: (3 * (n+1)) - sum of previous rolls
    next_roll = (3 * (len(rolls) + 1)) - sum(rolls)

    result = next_roll
    return result

print(solution())