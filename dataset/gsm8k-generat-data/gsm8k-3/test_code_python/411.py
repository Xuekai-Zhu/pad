def solution():
    """Max has 8 children and each of his children has the same number of children as he does except for 2 who have 5 children each. How many grandchildren does he have?"""
    # Define the number of children Max has
    num_children = 8

    # Calculate the number of grandchildren each of Max's children has
    # All of Max's children except for the two with 5 children each have num_children children
    num_grandchildren_per_child = num_children - 2 + (5 * 2)

    # Calculate the total number of grandchildren Max has
    total_grandchildren = num_children * num_grandchildren_per_child

    # Display the total number of grandchildren
    result = total_grandchildren
    return result

print(solution())