def solution():
    # Calculate the number of nephews Alden has now
    current_nephews = 50 * 2  # 50 nephews ten years ago is half the number of nephews Alden has now

    # Calculate the number of nephews Vihaan has
    vihaan_nephews = current_nephews + 60

    # Calculate the total number of nephews the two have altogether
    total_nephews = current_nephews + vihaan_nephews
    result = total_nephews
    return result

print(solution())