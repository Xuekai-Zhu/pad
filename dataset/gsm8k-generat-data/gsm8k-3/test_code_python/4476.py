def solution():
    """In spring, a family planted trees to capture the sun. They planted 3 times as many peaches as apricots. If 58 apricot trees were planted, how many trees were planted in total?"""
    # Define the ratio of peaches to apricots
    PEA_TO_APR_RATIO = 3

    # Define the number of apricot trees planted
    apricot_trees = 58

    # Calculate the number of peach trees planted
    peach_trees = PEA_TO_APR_RATIO * apricot_trees

    # Calculate the total number of trees planted
    total_trees = apricot_trees + peach_trees

    # Display the total number of trees planted
    result = total_trees
    return result

print(solution())