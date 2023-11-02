def solution():
    # Define the number of Gabriel's children and grandchildren
    gabriel_children = 2 # Assuming Gabriel has two children, John and Yasmin's dad
    gabriel_grandchildren = 6

    # Calculate the total number of grandchildren of Gabriel's children
    john_grandchildren = 2 * gabriel_grandchildren # John has twice the number of children that Yasmin has
    yasmin_grandchildren = gabriel_grandchildren - john_grandchildren # Yasmin's children have the remaining grandchildren

    # Calculate the number of Yasmin's children
    yasmin_children = yasmin_grandchildren // 2 # Each of Yasmin's children has two children of their own

    result = yasmin_children
    return result

print(solution())