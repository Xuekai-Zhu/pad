def solution():
    # Calculate the total square feet of wrapping paper needed by Carrie
    present1 = 2  # square feet of wrapping paper needed for first present
    present2 = (3/4) * present1  # square feet of wrapping paper needed for second present
    present3 = (present1 + present2) * 2  # square feet of wrapping paper needed for third present
    total_wrapping_paper = present1 + present2 + present3  # total square feet of wrapping paper needed

    result = total_wrapping_paper
    return result

print(solution())