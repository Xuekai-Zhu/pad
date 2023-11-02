def solution():
    
    beetles_per_bird = 12
    birds_per_snake = 3
    snakes_per_jaguar = 5
    jaguars_in_forest = 6
    snakes_eaten_per_day = jaguars_in_forest * snakes_per_jaguar
    birds_eaten_per_day = snakes_eaten_per_day * birds_per_snake
    beetles_eaten_per_day = birds_eaten_per_day * beetles_per_bird
    result = beetles_eaten_per_day
    return result

print(solution())