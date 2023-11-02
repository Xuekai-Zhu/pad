def solution():
    # Calculate the total number of sheets of paper in the two boxes
    total_sheets = 2 * 5 * 250

    # Calculate the number of newspapers that can be printed
    newspapers = total_sheets // 25

    # Return the result
    return newspapers

print(solution())