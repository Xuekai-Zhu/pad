def solution():
    """In a certain forest, there are 4 species of trees: oak, pine, spruce, and birch. There is a total of 4000 trees in the forest. Spruces make up 10% of all the trees, and pines 13%. There are as many oaks as spruces and pines put together. How many birches are there in the forest?"""
    total_trees = 4000
    spruce_percentage = 0.1
    pine_percentage = 0.13
    oak_percentage = (spruce_percentage + pine_percentage) / 2
    birch_percentage = 1 - spruce_percentage - pine_percentage - oak_percentage
    birch_trees = birch_percentage * total_trees
    result = birch_trees
    return result

print(solution())