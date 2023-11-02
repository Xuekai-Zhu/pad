def solution():
    soldiers_first_side = 4000
    soldiers_second_side = soldiers_first_side - 500
    food_first_side = soldiers_first_side * 10
    food_second_side = soldiers_second_side * 8
    total_food = food_first_side + food_second_side
    result = total_food
    return result

print(solution())