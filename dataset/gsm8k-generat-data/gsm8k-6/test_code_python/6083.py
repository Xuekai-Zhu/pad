def solution():
    # Get the sum of rolls so far and the number of rolls
    rolls = [1, 3, 2, 4, 3, 5, 3, 4, 4, 2]
    sum_rolls = sum(rolls)
    num_rolls = len(rolls)
    
    # Check what the next roll needs to be in order to have an average of 3
    # We want (sum_rolls + next_roll) / (num_rolls + 1) = 3
    # Simplifying this equation, we get next_roll = (3 * (num_rolls + 1) - sum_rolls)
    next_roll = (3 * (num_rolls + 1)) - sum_rolls
    result = next_roll
    return result

print(solution())