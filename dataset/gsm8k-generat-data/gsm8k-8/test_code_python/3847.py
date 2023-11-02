def solution():
    # Calculate the number of nice people for each name
    barry_nice = 24
    kevin_nice = 0.5 * 20
    julie_nice = 0.75 * 80
    joe_nice = 0.1 * 50

    # Calculate the total number of nice people
    total_nice = barry_nice + kevin_nice + julie_nice + joe_nice
    result = total_nice
    return result

print(solution())