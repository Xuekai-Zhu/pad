def solution():
    """A forester is planting trees. The forest already has 30 native trees. On Monday he triples the number of total trees in the forest by planting new trees. On Tuesday, he plants a third of the amount he planted on Monday. How many trees has the forester planted in total?"""
    native_trees = 30
    monday_planted = native_trees * 3 - native_trees
    tuesday_planted = monday_planted / 3
    total_planted = native_trees + monday_planted + tuesday_planted
    result = total_planted
    return result

print(solution())