def solution():
    total_grandkids = 6  # Gabriel has 6 grandkids
    john_children = 2 * yasmin_children  # John has twice the number of children that Yasmin has
    total_children = john_children + yasmin_children  # Total number of children between John and Yasmin

    # Find Yasmin's number of children by solving the equation
    # x + 2x = total_children
    yasmin_children = total_grandkids / 6  # Each child has 1 grandkid, and Gabriel has 6 grandkids
    result = yasmin_children
    return result

print(solution())