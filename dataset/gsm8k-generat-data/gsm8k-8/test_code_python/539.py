def solution():
    # Calculate how many trees were chopped down in total
    trees_chopped = 200 + 300
    
    # Calculate how many trees need to be planted for each tree chopped down
    trees_planted_per_chopped = 3  
    
    # Calculate how many trees the company needs to plant in total
    trees_planted = trees_chopped * trees_planted_per_chopped
    
    # Calculate how many more trees the company needs to plant
    trees_to_plant = trees_planted - trees_chopped
    
    result = trees_to_plant
    return result

print(solution())