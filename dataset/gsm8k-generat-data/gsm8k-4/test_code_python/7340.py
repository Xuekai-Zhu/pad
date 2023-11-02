def solution():
    """John and Yasmin's dad is named Gabriel. If John has twice the number of children that her sister has and Gabriel has six grandkids, how many children does Yasmin have?"""
    # Define the total number of grandchildren
    total_grandchildren = 6

    # Calculate the number of grandchildren of John and Yasmin combined
    john_grandchildren = 2 * yasmin_grandchildren
    combined_grandchildren = yasmin_grandchildren + john_grandchildren

    # Calculate the number of grandchildren of Gabriel's other children
    other_grandchildren = total_grandchildren - combined_grandchildren

    # Calculate the number of children of Gabriel's other children
    other_children = other_grandchildren // 2

    # Calculate the number of children of Yasmin
    yasmin_children = other_children + 1

    # Return the result
    result = yasmin_children
    return result

print(solution())