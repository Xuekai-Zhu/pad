def solution():
    
    beetles_eaten_per_bird = 12
    birds_eaten_per_snake = 3
    snakes_eaten_per_jaguar = 5
    jaguars_in_forest = 6
    beetles_eaten_per_day = beetles_eaten_per_bird * birds_eaten_per_snake * snakes_eaten_per_jaguar * jaguars_in_forest
    result = beetles_eaten_per_day
    return result

print(solution())