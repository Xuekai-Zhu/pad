def solution():
    """Max has 8 children and each of his children has the same number of children as he does except for 2 who have 5 children each. How many grandchildren does he have?"""
    num_children = 8
    num_grandchildren_per_child = num_children - 2  # all children except for 2 have num_children children each
    num_grandchildren = (num_children - 2) * num_grandchildren_per_child  # calculate total number of grandchildren
    num_grandchildren += 2 * 5  # add the 2 children with 5 children each
    result = num_grandchildren
    return result

print(solution())