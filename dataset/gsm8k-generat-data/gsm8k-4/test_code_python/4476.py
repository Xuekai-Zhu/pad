def solution():
    """In spring, a family planted trees to capture the sun. They planted 3 times as many peaches as apricots. If 58 apricot trees were planted, how many trees were planted in total?"""
    # Define the number of apricot trees planted
    apricot_trees = 58

    # Calculate the number of peach trees planted (3 times as many as apricot trees)
    peach_trees = 3 * apricot_trees

    # Calculate the total number of trees planted
    total_trees = apricot_trees + peach_trees

    # return the result
    result = total_trees
    return result

print(solution())