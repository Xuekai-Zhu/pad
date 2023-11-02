def solution():
    # Set up the system of equations
    # Let x = cost of one child's ticket
    # Let y = number of adult tickets
    # We have two equations:
    # x + 8y = 124 (total cost)
    # y + 11 = 10 + 11 (total number of people)

    # Simplify the second equation:
    # y + 11 = 21
    # y = 10

    # Substitute y = 10 into the first equation and solve for x:
    # x + 8(10) = 124
    # x + 80 = 124
    # x = 44/11

    result = round(44/11, 2)
    return result

print(solution())