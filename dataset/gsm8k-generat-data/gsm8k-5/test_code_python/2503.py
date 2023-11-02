def solution():
    # Calculate the current number of nephews Alden has
    current_nephews = 50 * 2  # Alden had 50 nephews 10 years ago, which is half of his current number of nephews

    # Calculate the number of nephews Vihaan has
    vihaan_nephews = current_nephews + 60  # Vihaan has 60 more nephews than Alden currently has

    # Calculate the total number of nephews the two have together
    total_nephews = current_nephews + vihaan_nephews
    result = total_nephews
    return result

print(solution())