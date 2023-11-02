def solution():
    # Max has 8-2 = 6 children with 8 children each
    num_grandchildren_per_child = 8
    num_children_with_5_grandchildren = 2
    num_grandchildren = 6*num_grandchildren_per_child + 5*num_children_with_5_grandchildren
    result = num_grandchildren
    return result

print(solution())