def solution():
    num_beetles_per_bird = 12
    num_birds_eaten_per_snake = 3
    num_snakes_eaten_per_jaguar = 5
    num_jaguars = 6

    # Calculate the total number of snakes eaten by all jaguars per day
    total_snakes_eaten = num_jaguars * num_snakes_eaten_per_jaguar

    # Calculate the total number of birds eaten by all snakes per day
    total_birds_eaten = total_snakes_eaten * num_birds_eaten_per_snake

    # Calculate the total number of beetles eaten by all birds per day
    total_beetles_eaten = total_birds_eaten * num_beetles_per_bird
    result = total_beetles_eaten
    return result

print(solution())