def solution():
    # Calculate the total number of appetizers needed
    total_appetizers = 6 * 30

    # Calculate the number of appetizers Patsy already has
    eggs = 3 * 12
    pigs = 2 * 12
    kebabs = 2 * 12
    total_existing = eggs + pigs + kebabs

    # Calculate the number of appetizers Patsy still needs to make
    remaining_appetizers = total_appetizers - total_existing
    dozens_needed = (remaining_appetizers // 12) + (remaining_appetizers % 12 > 0)
    result = dozens_needed
    return result

print(solution())