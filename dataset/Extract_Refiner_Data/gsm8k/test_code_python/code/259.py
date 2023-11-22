def solution():
    
    # Define the number of trees in Chris's yard
    chris_trees = 6

    # Calculate the number of trees in Ferdinand's yard
    fredinand_trees = chris_trees / 2

    # Calculate the number of trees in Harry's yard
    harry_trees = (2 * fredinand_trees) + 5

    # Calculate the difference in the number of trees between Harry and Ferdinand's yard
    difference = harry_trees - fredinand_trees

    # Display the difference in the number of trees
    result = difference
    return result

print(solution())