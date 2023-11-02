def solution():
    # Define the number of cheerleaders who need a size 2 and the total number of cheerleaders who need a size 6 or 12
    size2 = 4
    size6_or_12 = (19 - size2) / 2

    # Calculate the number of cheerleaders who need a size 6
    size6 = size6_or_12 - size6_or_12 / 2
    result = size6
    return result

print(solution())