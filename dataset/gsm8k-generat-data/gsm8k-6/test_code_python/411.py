def solution():
    # Calculate the total number of grandchildren Max has
    grandchildren_per_child = 8  # each of Max's children has 8 children
    two_children_with_5_each = 2 * 5  # two of Max's children have 5 children each
    total_grandchildren = (8-2) * grandchildren_per_child + two_children_with_5_each  # total number of grandchildren
    result = total_grandchildren
    return result

print(solution())