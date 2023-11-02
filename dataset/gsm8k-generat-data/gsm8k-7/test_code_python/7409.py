def solution():
    num_rolls = 1000
    squares_per_roll = 300

    num_uses_per_day = 3
    squares_per_use = 5

    # Calculate the total number of squares of toilet paper that Bill uses every day
    total_squares_per_day = num_uses_per_day * squares_per_use

    # Calculate the total number of squares of toilet paper that Bill will use during his whole supply
    total_squares_used = total_squares_per_day * num_days

    # Calculate the number of days that the toilet paper supply will last
    num_days = (num_rolls * squares_per_roll) / total_squares_used
    
    result = num_days
    return result

print(solution())