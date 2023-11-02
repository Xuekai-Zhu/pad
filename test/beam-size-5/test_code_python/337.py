def solution():
    
    # Define the weight of the pink frog
    frog_weight = 50

    # Calculate the weight of the yellow snake
    snake_weight = frog_weight - 10

    # Calculate the weight of the red bird
    bird_weight = frog_weight + 20

    # Calculate the weight of each animal
    animal_weight = frog_weight + snake_weight + bird_weight

    # Display the weight of each animal
    result = animal_weight
    return result

print(solution())