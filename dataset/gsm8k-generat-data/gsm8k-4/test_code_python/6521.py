def solution():
    """In a certain forest, there are 4 species of trees: oak, pine, spruce, and birch. There is a total of 4000 trees in the forest. Spruces make up 10% of all the trees, and pines 13%. There are as many oaks as spruces and pines put together. How many birches are there in the forest?"""
    # Define the total number of trees and the percentage of spruces and pines
    total_trees = 4000
    spruce_percentage = 0.1
    pine_percentage = 0.13

    # Calculate the number of spruces and pines
    spruces = int(total_trees * spruce_percentage)
    pines = int(total_trees * pine_percentage)

    # Calculate the number of oaks
    oaks = spruces + pines

    # Calculate the number of birches
    birches = total_trees - spruces - pines - oaks

    # return the result
    result = birches
    return result

print(solution())