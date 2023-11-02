def solution():
    counted_toddlers = 26
    double_counted = 8
    missed = 3

    # Subtract the double-counted toddlers
    real_counted = counted_toddlers - double_counted

    # Add the missed toddlers
    real_counted += missed

    # Calculate the total number of toddlers
    total_toddlers = real_counted
    result = total_toddlers
    return result

print(solution())