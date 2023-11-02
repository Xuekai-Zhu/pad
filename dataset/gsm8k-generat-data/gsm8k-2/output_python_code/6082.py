def solution():
    """Ronald is rolling a die and won't stop rolling until the average of all his rolls is a 3. He rolls a 1, a 3, a 2, a 4, a 3, a 5, a 3, a 4, a 4 and a 2. What does he need to roll on the next roll to be able to stop?"""
    rolls = [1, 3, 2, 4, 3, 5, 3, 4, 4, 2]
    current_sum = sum(rolls)
    current_average = current_sum / len(rolls)
    needed_sum = 3 * (len(rolls) + 1) - current_sum
    next_roll_needed = needed_sum / (len(rolls) + 1 - len(rolls))
    result = next_roll_needed
    return result

print(solution())