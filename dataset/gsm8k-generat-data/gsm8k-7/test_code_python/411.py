def solution():
    num_children = 8
    num_grandchildren_per_child = num_children - 2
    num_grandchildren = (num_children - 2) * (num_grandchildren_per_child) + (2 * 5) #2 children have 5 children each
    result = num_grandchildren
    return result

print(solution())