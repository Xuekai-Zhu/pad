def solution():
    """John and Yasmin's dad is named Gabriel. If John has twice the number of children that her sister has and Gabriel has six grandkids, how many children does Yasmin have?"""
    # Define the number of Gabriel's children and grandchildren
    gabriel_children = 2

    # Calculate the number of John's children
    john_children = gabriel_children * 2

    # Calculate the total number of grandchildren
    total_grandchildren = gabriel_children + john_children

    # Calculate the number of Yasmin's children
    yasmin_children = total_grandchildren - gabriel_children

    # Display the number of Yasmin's children
    result = yasmin_children
    return result

print(solution())