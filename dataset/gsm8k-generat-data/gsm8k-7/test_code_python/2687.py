def solution():
    native_trees = 30

    # On Monday, the number of total trees is tripled, so the new total number of trees becomes 3 * (native_trees + x)
    x = (3 * native_trees) - native_trees

    # On Tuesday, the forester plants a third of the amount he planted on Monday, which is (1/3)*x
    trees_planted_tuesday = (1/3) * x

    # Total number of trees planted is native trees + trees planted on Monday + trees planted on Tuesday
    total_trees_planted = native_trees + x + trees_planted_tuesday
    
    result = total_trees_planted
    return result

print(solution())