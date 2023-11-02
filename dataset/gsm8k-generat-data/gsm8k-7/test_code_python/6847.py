def solution():
    num_soldiers_1st_side = 4000
    num_soldiers_2nd_side = num_soldiers_1st_side - 500
    food_per_soldier = 10
    food_per_soldier_2nd_side = food_per_soldier - 2

    # Calculate the total amount of food needed by the first side
    total_food_1st_side = num_soldiers_1st_side * food_per_soldier

    # Calculate the total amount of food needed by the second side
    total_food_2nd_side = num_soldiers_2nd_side * food_per_soldier_2nd_side

    # Calculate the total amount of food needed by both sides
    total_food = total_food_1st_side + total_food_2nd_side
    result = total_food
    return result

print(solution())