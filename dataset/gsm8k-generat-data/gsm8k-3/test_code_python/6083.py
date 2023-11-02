def solution():
    """Ronald is rolling a die and won't stop rolling until the average of all his rolls is a 3. He rolls a 1, a 3, a 2, a 4, a 3, a 5, a 3, a 4, a 4 and a 2. What does he need to roll on the next roll to be able to stop?"""
    # Calculate the current average of all rolls
    rolls = [1, 3, 2, 4, 3, 5, 3, 4, 4, 2]
    current_average = sum(rolls)/len(rolls)

    # Calculate the sum of all rolls necessary to reach an average of 3
    rolls_sum_needed = 3*(len(rolls) + 1) - sum(rolls)

    # Calculate the needed roll to reach an average of 3
    needed_roll = rolls_sum_needed/(len(rolls)+1) 

    # Display the needed roll
    result = needed_roll
    return result

print(solution())