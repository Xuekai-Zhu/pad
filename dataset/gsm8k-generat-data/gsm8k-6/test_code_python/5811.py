def solution():
    # Calculate the total earned in September for mowing lawns and pulling weeds
    total_sept_earned = 4 * 25 + 8 * 3 # 25 hours of mowing lawns at $4/hour and 3 hours of pulling weeds at $8/hour

    # Calculate the total earned in October assuming the same number of hours worked
    total_oct_earned = total_sept_earned

    # Calculate the total earned in September and October together
    total_earned = total_sept_earned + total_oct_earned
    result = total_earned
    return result

print(solution())