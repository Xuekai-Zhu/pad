def solution():
    # Calculate the total number of soldiers in the second side
    soldiers_second_side = 4000 - 500  

    # Calculate the total amount of food needed by both sides
    food_first_side = 10 * 4000  # 4000 soldiers in the first side
    food_second_side = 8 * soldiers_second_side  # each soldier on the second side is given 2 pounds less food
    total_food = food_first_side + food_second_side

    result = total_food
    return result

print(solution())