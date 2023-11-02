def solution():
    # Calculate the amount of wrapping paper needed for the first present
    present1 = 2

    # Calculate the amount of wrapping paper needed for the second present
    present2 = 3/4 * present1

    # Calculate the total amount of wrapping paper needed for the first two presents
    total_present12 = present1 + present2

    # Calculate the amount of wrapping paper needed for the third present
    present3 = 2 * total_present12

    # Calculate the total amount of wrapping paper needed for all three presents
    total_paper = present1 + present2 + present3
    result = total_paper
    return result

print(solution())