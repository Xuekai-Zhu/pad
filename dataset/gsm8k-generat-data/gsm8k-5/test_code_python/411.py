def solution():
    num_grandchildren_per_child = 8  # Each of Max's children has 8 children
    num_children_with_5_grandchildren = 2  # 2 of Max's children have 5 children each
    num_children_with_8_grandchildren = 8 - num_children_with_5_grandchildren  # The rest of Max's children have 8 children each

    # Calculate the total number of grandchildren
    total_grandchildren = (num_children_with_8_grandchildren * num_grandchildren_per_child) + (num_children_with_5_grandchildren * 5)

    result = total_grandchildren
    return result

print(solution())