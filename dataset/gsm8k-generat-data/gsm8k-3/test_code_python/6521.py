def solution():
    """In a certain forest, there are 4 species of trees: oak, pine, spruce, and birch. There is a total of 4000 trees in the forest. Spruces make up 10% of all the trees, and pines 13%. There are as many oaks as spruces and pines put together. How many birches are there in the forest?"""
    # Define the percentages of each type of tree
    SPRUCE_PERCENT = 0.10
    PINE_PERCENT = 0.13

    # Calculate the number of spruce trees in the forest
    spruce_count = int(4000 * SPRUCE_PERCENT)

    # Calculate the number of pine trees in the forest
    pine_count = int(4000 * PINE_PERCENT)

    # Calculate the number of oak trees in the forest
    oak_count = spruce_count + pine_count

    # Calculate the number of birch trees in the forest
    birch_count = 4000 - (spruce_count + pine_count + oak_count)

    # Display the number of birch trees
    result = birch_count
    return result

print(solution())