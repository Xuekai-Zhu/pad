def solution():
    beetles_per_bird = 12  # Each bird eats 12 beetles per day
    birds_per_snake = 3  # Each snake eats 3 birds per day
    snakes_per_jaguar = 5  # Each jaguar eats 5 snakes per day
    jaguars_in_forest = 6  # There are 6 jaguars in the forest

    # Calculate the total number of snakes in the forest
    total_snakes = jaguars_in_forest * snakes_per_jaguar

    # Calculate the total number of birds in the forest
    total_birds = total_snakes * birds_per_snake

    # Calculate the total number of beetles eaten each day
    total_beetles = total_birds * beetles_per_bird
    result = total_beetles
    return result

print(solution())