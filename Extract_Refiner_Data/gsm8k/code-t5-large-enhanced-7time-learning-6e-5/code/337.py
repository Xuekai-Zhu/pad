def solution():
    
    # Define the weight of the pink frog
    frog_weight = 50

    # Calculate the weight of the yellow snake and red bird
    snake_weight = frog_weight + 10
    red_bird_weight = frog_weight + 20

    # Calculate the total weight of the container
    total_weight = frog_weight + snake_weight + red_bird_weight

    # Calculate the weight of each animal in the container
    weight_per_animal = total_weight / 20

    # Display the weight of each animal in the container
    result = weight_per_animal
    return result

print(solution())