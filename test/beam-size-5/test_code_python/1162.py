def solution():
    
    # Define the number of fruits produced in each year
    tree_5_fruits = 50
    tree_6_fruits = tree_5_fruits * 3
    tree_7_fruits = tree_6_fruits * 7
    tree_8_fruits = tree_7_fruits - 200
    tree_10_fruits = tree_10_fruits * 20

    # Calculate the total number of fruits produced by the tree
    total_fruits = tree_5_fruits + tree_6_fruits + tree_7_fruits + tree_8_fruits + tree_10_fruits

    # Display the total number of fruits produced
    result = total_fruits
    return result

print(solution())