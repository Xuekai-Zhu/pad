def solution():
    """In a certain forest, there are 4 species of trees: oak, pine, spruce, and birch. There is a total of 4000 trees in the forest. Spruces make up 10% of all the trees, and pines 13%. There are as many oaks as spruces and pines put together. How many birches are there in the forest?"""
    total_trees = 4000
    spruce_percent = 0.1
    pine_percent = 0.13

    spruce_trees = total_trees * spruce_percent
    pine_trees = total_trees * pine_percent
    oak_trees = (spruce_trees + pine_trees) / 2
    birch_trees = total_trees - spruce_trees - pine_trees - oak_trees

    result = int(birch_trees)
    return result

print(solution())