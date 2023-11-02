def solution():
    
    rolls = [1, 3, 2, 4, 3, 5, 3, 4, 4, 2]
    current_sum = sum(rolls)
    current_average = current_sum / len(rolls)
    needed_sum = 3 * (len(rolls) + 1) - current_sum
    next_roll_needed = needed_sum / (len(rolls) + 1 - len(rolls))
    result = next_roll_needed
    return result

print(solution())