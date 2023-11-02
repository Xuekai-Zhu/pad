def solution():
    # Calculate the number of snakes eaten per day by all jaguars
    snakes_eaten_per_jaguar = 5  # Each jaguar eats 5 snakes per day
    total_snakes_eaten = snakes_eaten_per_jaguar * 6  # There are 6 jaguars in the forest
    # Calculate the number of birds eaten per day by all snakes
    birds_eaten_per_snake = 3  # Each snake eats 3 birds per day
    total_birds_eaten = birds_eaten_per_snake * total_snakes_eaten
    # Calculate the number of beetles eaten per day by all birds
    beetles_eaten_per_bird = 12  # Each bird eats 12 beetles per day
    total_beetles_eaten = beetles_eaten_per_bird * total_birds_eaten
    result = total_beetles_eaten
    return result

print(solution())