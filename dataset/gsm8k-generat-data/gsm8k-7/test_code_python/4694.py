def solution():
    initial_leaves = 1000
    first_week_shed = 2 / 5
    second_week_shed = 0.4
    third_week_shed = 0

    # Calculate the number of leaves after the first week
    first_week_leaves = initial_leaves * (1 - first_week_shed)

    # Calculate the number of leaves after the second week
    second_week_leaves = first_week_leaves * (1 - second_week_shed)

    # Calculate the number of leaves shed on the third week
    third_week_shed_leaves = second_week_leaves * (3 / 4)

    # Calculate the number of leaves remaining after the third week
    remaining_leaves = second_week_leaves - third_week_shed_leaves
    result = remaining_leaves
    return result

print(solution())