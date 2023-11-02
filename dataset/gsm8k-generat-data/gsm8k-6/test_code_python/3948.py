def solution():
    # Calculate John's new lifting capacity
    clean_jerk = 80 * 2  # John double his clean and jerk
    snatch = 50 * 1.8  # John increased his snatch by 80%
    new_total = clean_jerk + snatch  # John's new combined total lifting capacity
    
    result = new_total
    return result

print(solution())