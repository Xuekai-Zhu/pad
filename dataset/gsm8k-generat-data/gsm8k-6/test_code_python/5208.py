def solution():
    # Let's assume the number of adult tickets sold is x and the number of child tickets sold is y
    # We have two equations:
    # x + y = total number of tickets sold
    # 15x + 8y = 720 (total amount paid for all tickets sold)

    # We know that there are 25 more adults than children
    # Therefore, x = y + 25

    # Substituting x in the first equation, we get:
    # y + 25 + y = total number of tickets sold
    # 2y + 25 = total number of tickets sold

    # Substituting x and y in the second equation, we get:
    # 15(y + 25) + 8y = 720
    # 15y + 375 + 8y = 720
    # 23y = 345
    # y = 15

    # Therefore, there are 15 children in the group
    result = 15
    return result

print(solution())