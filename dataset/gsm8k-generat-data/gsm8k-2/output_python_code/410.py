def solution():
    """Max has 8 children and each of his children has the same number of children as he does
    except for 2 who have 5 children each. How many grandchildren does he have?"""
    max_children = 8
    children_grandchildren_ratio = 1  # each child has one child
    num_special_children = 2
    num_special_grandchildren = 5
    num_regular_children = max_children - num_special_children
    num_regular_grandchildren = num_regular_children * children_grandchildren_ratio
    total_grandchildren = num_regular_grandchildren + (num_special_children * num_special_grandchildren)
    result = total_grandchildren
    return result

print(solution())