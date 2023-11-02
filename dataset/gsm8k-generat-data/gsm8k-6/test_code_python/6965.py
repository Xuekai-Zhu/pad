def solution():
    # Calculate the total number of sheets of paper Julie bought
    total_sheets = 2 * 5 * 250

    # Calculate the total number of newspapers Julie can print
    newspapers = total_sheets // 25  # integer division was used to get the maximum number of newspapers
    result = newspapers
    return result

print(solution())