def solution():
    # Calculate the number of apples Greg and Sarah each get
    apples_each = 18 / 2

    # Calculate the number of apples Susan has
    susan_apples = 2 * apples_each

    # Calculate the number of apples Mark has
    mark_apples = susan_apples - 5

    # Calculate the total number of apples in the group
    total_apples = apples_each * 2 + susan_apples + mark_apples

    # Calculate the number of apples left over for the pie
    apples_left_over = total_apples - 40
    result = apples_left_over
    return result

print(solution())