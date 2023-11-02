def solution():
    """Max has 8 children and each of his children has the same number of children as he does except for 2 who have 5 children each. How many grandchildren does he have?"""
    # Define the number of children Max has
    num_children = 8

    # Define the number of grandchildren each child has
    grandchildren_per_child = num_children - 2

    # Calculate the total number of grandchildren
    total_grandchildren = (num_children - 2) * (num_children - 2) + 5*2

    # return the result
    result = total_grandchildren
    return result

print(solution())